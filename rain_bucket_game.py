import pygame
import sys
import random

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH = 900
HEIGHT = 700
size = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(size)
pygame.display.set_caption("Raindrops Game")  # Set a title for the window
pygame.display.update()

# Game variables
game_over = False
score = 0

# Raindrop settings
RAINSIZE = 10
rain_list = []

# Game settings
SPEED = 1
AMOUNT = 5

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Generate new raindrops
    for i in range(AMOUNT):
        x = random.randrange(0, WIDTH)
        y = random.randrange(0, HEIGHT)
        rain_list.append([x, y])

    # Move raindrops down the screen
    for drop in rain_list:
        drop[1] += SPEED

        # Check if raindrop goes off screen
        if drop[1] > HEIGHT:
            rain_list.remove(drop)
            score += 1  # Increment score for each raindrop that goes off screen

    # Clear screen and draw raindrops
    SCREEN.fill(BLUE)
    for drop in rain_list:
        pygame.draw.circle(SCREEN, RED, drop, RAINSIZE)

    # Display score
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score: {score}', True, RED)
    SCREEN.blit(text, (10, 10))

    pygame.display.update()

    # Adjust game speed (optional)
    pygame.time.Clock().tick(30)  # Limit to 30 frames per second

# Quit pygame properly
pygame.quit()
sys.exit()
