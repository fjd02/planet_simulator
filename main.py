import pygame
from planet import Planet

pygame.init()

# STATIC VARIABLES
WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

## COLORS
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (170, 170, 0)
DARK_BLUE = (100, 200, 255)
BLUE = (100, 149, 237)
LIGHT_BLUE = (100, 149, 175)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
PURPLE = (130, 0, 180)


# Pygame Event Loop
def main():
    run = True
    clock = pygame.time.Clock()

    # Sun and Planets
    sun = Planet(0, 0, 6, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    mercury = Planet(0.387 * Planet.AU, 0, 2, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.870 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 4, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.020 * 1000

    earth = Planet(-1 * Planet.AU, 0, 5, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.780 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 3, RED, 6.39 * 10**23)
    mars.y_vel = 24.070 * 1000

    jupiter = Planet(5.203 * Planet.AU, 0, 14, PURPLE, 1.8981 * 10**27)
    jupiter.y_vel = -13.070 * 1000

    saturn = Planet(9.537 * Planet.AU, 0, 12, LIGHT_YELLOW, 5.68 * 10**26)
    saturn.y_vel = -9.690 * 1000

    uranus = Planet(-19.191 * Planet.AU, 0, 8, LIGHT_BLUE, 8.68 * 10**25)
    uranus.y_vel = 6.810 * 1000

    neptune = Planet(30.071 * Planet.AU, 0, 7, DARK_BLUE, 1.02 * 10**26)
    neptune.y_vel = -5.430 * 1000

    planets = [sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN, WIDTH, HEIGHT)

        pygame.display.update()

    pygame.quit()

main()
