# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *
def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #Exits the function and stops the game loop

        screen.fill((0, 0, 0)) #Fills the screen with black
        pygame.display.flip()  #Updates the display

if __name__ == "__main__":
    main()
