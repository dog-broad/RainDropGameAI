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

# Fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# Function to create raindrops
def create_raindrop():
    x = random.randint(0, WIDTH - 30)
    y = random.randint(-HEIGHT, 0)
    return {'rect': pygame.Rect(x, y, 30, 30), 'speed': random.randint(5, 15)}

# Function to display start screen
def show_start_screen():
    screen.fill(WHITE)
    start_text = large_font.render("Rain Bucket Game", True, BLUE)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(start_text, start_rect)

    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(screen, BLUE, start_button)
    start_button_text = font.render("Start Game", True, WHITE)
    start_button_text_rect = start_button_text.get_rect(center=start_button.center)
    screen.blit(start_button_text, start_button_text_rect)

    pygame.display.flip()

    # Wait for the player to click start
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    return

# Main game loop
def game_loop():
    global score
    bucket_rect = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 80, 80, 80)
    raindrops = []
    start_time = pygame.time.get_ticks()
    game_over = False

    while not game_over:
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
        score_text = font.render(f'Score: {score}', True, BLUE)
        screen.blit(score_text, (10, 10))

        # Display time remaining
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        time_text = font.render(f'Time: {60 - elapsed_time}', True, BLUE)
        screen.blit(time_text, (WIDTH - 120, 10))

        # Check game end condition
        if elapsed_time >= 60:
            game_over_text = large_font.render("Game Over", True, BLUE)
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(game_over_text, game_over_rect)

            final_score_text = font.render(f'Final Score: {score}', True, BLUE)
            final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            screen.blit(final_score_text, final_score_rect)

            pygame.display.flip()
            pygame.time.delay(3000)  # Pause for 3 seconds
            return

        pygame.display.flip()
        clock.tick(FPS)

# Game execution
show_start_screen()
game_loop()

pygame.quit()
sys.exit()
