import pygame
import random  # Import the random module for angle generation
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS  # Import the minimum radius constant

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Moves the asteroid in a straight line at constant speed
        self.position += self.velocity * dt

    def split(self):
        # Kill the current asteroid
        self.kill()

        # If the asteroid's radius is less than or equal to ASTEROID_MIN_RADIUS, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Define the new radius for the split asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate a random angle to split the velocity
        angle = random.uniform(20, 50)

        # Create two new velocity vectors, rotated by `angle` and `-angle`
        velocity_1 = self.velocity.rotate(angle) * 1.2  # Increase speed by 1.2x
        velocity_2 = self.velocity.rotate(-angle) * 1.2  # In opposite direction

        # Create two new asteroids at the same position but with the new radius and velocities
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = velocity_1

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = velocity_2
