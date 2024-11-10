# this allows us to use code from the open-source pygame library throughout this file
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate the player at the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Groups to manage updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Add the player to both groups
    updatable.add(player)
    drawable.add(player)

    # Set containers for Asteroid and AsteroidField classes
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Create an instance of AsteroidField
    asteroid_field = AsteroidField()

    # Group to hold all asteroids
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # Group to hold Shot
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)



    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Fills the screen with black

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    asteroid.split()  # Call split instead of kill
                    bullet.kill()    # Remove the bullet

        # Check for collisions between asteroids and the player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return  # Exit the game immediately on collision



        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()    # Updates the display
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and update dt

if __name__ == "__main__":
    main()
