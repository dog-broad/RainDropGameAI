import pygame
import sys
import random
import math

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
raindrop_frequency = 25
bucket_speed = 15  # Adjusted for smoother movement

# Control modes
HUMAN_CONTROL = 0
AI_CONTROL = 1

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
    speed = random.randint(5, 15)
    return {'rect': pygame.Rect(x, y, 30, 30), 'speed': speed, 'falling': True, 'direction': random.choice([-1, 1])}

# Function to display start screen and select control mode
def show_start_screen():
    screen.fill(WHITE)
    start_text = large_font.render("Rain Bucket Game", True, BLUE)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(start_text, start_rect)

    human_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
    pygame.draw.rect(screen, BLUE, human_button)
    human_button_text = font.render("Human Control", True, WHITE)
    human_button_text_rect = human_button_text.get_rect(center=human_button.center)
    screen.blit(human_button_text, human_button_text_rect)

    ai_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50)
    pygame.draw.rect(screen, BLUE, ai_button)
    ai_button_text = font.render("AI Control", True, WHITE)
    ai_button_text_rect = ai_button_text.get_rect(center=ai_button.center)
    screen.blit(ai_button_text, ai_button_text_rect)

    pygame.display.flip()

    # Wait for the player to click on a control mode
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if human_button.collidepoint(event.pos):
                    return HUMAN_CONTROL
                elif ai_button.collidepoint(event.pos):
                    return AI_CONTROL

# Function to display game over screen with return to menu option
def show_game_over_screen():
    screen.fill(WHITE)
    game_over_text = large_font.render("Game Over", True, BLUE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_over_text, game_over_rect)

    final_score_text = font.render(f'Final Score: {score}', True, BLUE)
    final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(final_score_text, final_score_rect)

    return_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(screen, BLUE, return_button)
    return_button_text = font.render("Return to Menu", True, WHITE)
    return_button_text_rect = return_button_text.get_rect(center=return_button.center)
    screen.blit(return_button_text, return_button_text_rect)

    pygame.display.flip()

    # Wait for the player to click on return to menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if return_button.collidepoint(event.pos):
                    return True  # Return to menu

# Function to calculate distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Main game loop with human or AI control based on player choice
def game_loop(game_duration, control_mode):
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
            if raindrop['falling']:
                raindrop['rect'].move_ip(0, raindrop['speed'])

        # Human control
        if control_mode == HUMAN_CONTROL:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and bucket_rect.left > 0:
                bucket_rect.move_ip(-bucket_speed, 0)
            if keys[pygame.K_RIGHT] and bucket_rect.right < WIDTH:
                bucket_rect.move_ip(bucket_speed, 0)

        # AI control
        elif control_mode == AI_CONTROL:
            if raindrops:
                closest_raindrop = min(raindrops, key=lambda r: distance(r['rect'].center, bucket_rect.center))
                target_x = closest_raindrop['rect'].centerx
                if target_x < bucket_rect.centerx and bucket_rect.left > 0:
                    bucket_rect.move_ip(-bucket_speed, 0)
                elif target_x > bucket_rect.centerx and bucket_rect.right < WIDTH:
                    bucket_rect.move_ip(bucket_speed, 0)

        # Check collision with bucket
        for raindrop in raindrops[:]:
            if raindrop['rect'].colliderect(bucket_rect):
                raindrops.remove(raindrop)
                score += 1

        # Remove raindrops that go off screen
        for raindrop in raindrops[:]:
            if raindrop['rect'].top > HEIGHT:
                raindrops.remove(raindrop)

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
        time_text = font.render(f'Time: {game_duration - elapsed_time}', True, BLUE)
        screen.blit(time_text, (WIDTH - 120, 10))

        # Check game end condition
        if elapsed_time >= game_duration:
            if show_game_over_screen():
                return True  # Return to menu

        pygame.display.flip()
        clock.tick(FPS)

# Game execution with option for Human or AI controls
while True:
    control_mode = show_start_screen()
    if game_loop(30, control_mode):  # Set the game duration here (in seconds)
        continue  # Return to menu

pygame.quit()
sys.exit()
