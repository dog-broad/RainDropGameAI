import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game variables
score = 0
speed = 5
raindrop_frequency = 25
bucket_speed = 10

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Bucket Game")
clock = pygame.time.Clock()

# Function to create raindrops
def create_raindrop():
    x = random.randint(0, WIDTH - 30)
    y = random.randint(-HEIGHT, 0)
    return {'rect': pygame.Rect(x, y, 30, 30), 'speed': random.randint(5, 15)}

# Main game loop
def game_loop():
    global score
    bucket_rect = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 80, 80, 80)
    raindrops = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Generate raindrops
        if random.randint(1, raindrop_frequency) == 1:
            raindrops.append(create_raindrop())

        # Move raindrops
        for raindrop in raindrops:
            raindrop['rect'].move_ip(0, raindrop['speed'])

        # Check collision with bucket
        for raindrop in raindrops[:]:
            if bucket_rect.colliderect(raindrop['rect']):
                raindrops.remove(raindrop)
                score += 1

        # Remove raindrops that go off screen
        for raindrop in raindrops[:]:
            if raindrop['rect'].top > HEIGHT:
                raindrops.remove(raindrop)

        # Move bucket based on user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bucket_rect.left > 0:
            bucket_rect.move_ip(-bucket_speed, 0)
        if keys[pygame.K_RIGHT] and bucket_rect.right < WIDTH:
            bucket_rect.move_ip(bucket_speed, 0)

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, bucket_rect)  # Draw bucket
        for raindrop in raindrops:
            pygame.draw.circle(screen, YELLOW, raindrop['rect'].center, 15)  # Draw raindrop

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, BLUE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

# Start the game loop
game_loop()
