import pygame, math
from planet import Planet

pygame.init()

# STATIC VARIABLES
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

## COLORS
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (170, 170, 0)
DARK_BLUE = (100, 149, 255)
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
    sun = Planet(0, 0, 35, YELLOW, 1.98892 * 10**30)
    sun.sun = True
    mercury = Planet(0.3 * Planet.AU, 0, 4, DARK_GREY, 3.30 * 10**23)
    venus = Planet(0.7 * Planet.AU, 0, 7, WHITE, 4.8685 * 10**24)
    earth = Planet(-0.9 * Planet.AU, 0, 8, BLUE, 5.9742 * 10**24)
    mars = Planet(-1.3 * Planet.AU, 0, 5, RED, 6.39 * 10**23)
    jupiter = Planet(0, -1.6 * Planet.AU, 25, PURPLE, 1.90 * 10*27)
    saturn = Planet(0, 1.7 * Planet.AU, 22, LIGHT_YELLOW, 5.68 * 10**26)
    uranus = Planet(-2 * Planet.AU, 0, 14, LIGHT_BLUE, 8.68 * 10**25)
    neptune = Planet(2.1 * Planet.AU, 0, 13, DARK_BLUE, 1.02* 10**26)

    planets = [sun, earth, mars, mercury, venus, jupiter, saturn, uranus, neptune]

    while run:
        clock.tick(60)
        #WIN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.draw(WIN, WIDTH, HEIGHT)

        pygame.display.update()

    pygame.quit()

main()
