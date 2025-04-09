import pygame, math

class Planet:
    # STATIC VARIABLES
    AU = 149.6e6 * 1000 # Astronomical Units (Aprox. distance from the planet to the Sun).
    G = 6.67428e-11 # Gravitational Constant. Use to find the force of attraction between objects.
    SCALE = 24 / AU # 1 AU = 100 pixels.
    TIMESTEP = 3600*24 # One Day.

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win, width, height):
        x = self.x * self.SCALE + width / 2
        y = self.y * self.SCALE + height / 2

        # Drawing orbits
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + width / 2
                y = y * self.SCALE + height / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 1)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        # We calculate the distance between the sun and the other planet.
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # If the object is the sun, we store the distance.
        if other.sun:
            self.distance_to_sun = distance

        # We calculate the force of attraction.
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
        