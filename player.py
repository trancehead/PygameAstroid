import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from shot import Shot
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initialize rotation to 0
        self.shoot_timer = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate counter-clockwise

        # Rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate clockwise

        # Move forward
        if keys[pygame.K_w]:
            self.move(dt)  # Move forward when W is pressed

        # Move backward
        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward when S is pressed

        # Shoot when the spacebar is pressed
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Decrease the shooting timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    def move(self, dt):
        # Create a forward vector pointing in the direction of the player's rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Adjust the player's position by the forward vector scaled by PLAYER_SPEED and dt
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        print("Shoot Timer:", self.shoot_timer)  # Debug print
        if self.shoot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

