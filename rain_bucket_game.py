import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize sound mixer

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)  # Color for Human Control bucket
GREEN = (0, 255, 0)  # Color for AI Control bucket

# Sound effects
try:
    game_over_sound = pygame.mixer.Sound('./assets/game_over_sound.wav')
    catch_sound = pygame.mixer.Sound('./assets/catch_sound.wav')
except pygame.error as e:
    print(f"Sound file error: {e}")
    game_over_sound = None
    catch_sound = None

# Game variables
score_human = 0
score_ai = 0
raindrop_frequency = 25
bucket_speed = 15  # Adjusted for smoother movement

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Bucket Game - Human vs. AI")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 64)

# Function to create raindrops
def create_raindrop():
    x = random.randint(0, WIDTH - 30)
    y = random.randint(-HEIGHT, 0)
    speed = random.randint(5, 15)
    return {'rect': pygame.Rect(x, y, 30, 30), 'speed': speed, 'falling': True, 'direction': random.choice([-1, 1])}

# Function to display game over screen with return to menu option
def show_game_over_screen():
    global score_human, score_ai
    screen.fill(WHITE)
    game_over_text = large_font.render("Game Over", True, BLUE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(game_over_text, game_over_rect)

    human_score_text = font.render(f'Human Score: {score_human}', True, RED)
    human_score_rect = human_score_text.get_rect(center=(WIDTH // 4, HEIGHT // 2))
    screen.blit(human_score_text, human_score_rect)

    ai_score_text = font.render(f'AI Score: {score_ai}', True, GREEN)
    ai_score_rect = ai_score_text.get_rect(center=(WIDTH // 4 * 3, HEIGHT // 2))
    screen.blit(ai_score_text, ai_score_rect)

    if score_human > score_ai:
        result_text = large_font.render("Human Wins!", True, RED)
    elif score_ai > score_human:
        result_text = large_font.render("AI Wins!", True, GREEN)
    else:
        result_text = large_font.render("It's a Tie!", True, BLUE)
    
    result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(result_text, result_rect)

    return_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
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

# AI control logic
def ai_control(bucket_rect, raindrops):
    if raindrops:
        closest_raindrop = min(raindrops, key=lambda r: distance(r['rect'].center, bucket_rect.center))
        target_x = closest_raindrop['rect'].centerx
        if target_x < bucket_rect.centerx and bucket_rect.left > 0:
            bucket_rect.move_ip(-bucket_speed, 0)
        elif target_x > bucket_rect.centerx and bucket_rect.right < WIDTH:
            bucket_rect.move_ip(bucket_speed, 0)

# Game loop for Human vs. AI mode
def game_loop_human_vs_ai(game_duration):
    global score_human, score_ai

    bucket_rect_human = pygame.Rect(WIDTH // 4 - 40, HEIGHT - 80, 80, 80)
    bucket_rect_ai = pygame.Rect(WIDTH // 4 * 3 - 40, HEIGHT - 80, 80, 80)
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bucket_rect_human.left > 0:
            bucket_rect_human.move_ip(-bucket_speed, 0)
        if keys[pygame.K_RIGHT] and bucket_rect_human.right < WIDTH:
            bucket_rect_human.move_ip(bucket_speed, 0)

        # AI control
        ai_control(bucket_rect_ai, raindrops)

        # Check collision with human bucket
        for raindrop in raindrops[:]:
            if raindrop['rect'].colliderect(bucket_rect_human):
                raindrops.remove(raindrop)
                score_human += 1
                if catch_sound:
                    catch_sound.play()  # Play catch sound

        # Check collision with AI bucket
        for raindrop in raindrops[:]:
            if raindrop['rect'].colliderect(bucket_rect_ai):
                raindrops.remove(raindrop)
                score_ai += 1
                if catch_sound:
                    catch_sound.play()  # Play catch sound

        # Remove raindrops that go off screen
        for raindrop in raindrops[:]:
            if raindrop['rect'].top > HEIGHT:
                raindrops.remove(raindrop)

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, bucket_rect_human)  # Draw human bucket
        pygame.draw.rect(screen, GREEN, bucket_rect_ai)  # Draw AI bucket
        for raindrop in raindrops:
            pygame.draw.circle(screen, YELLOW, raindrop['rect'].center, 15)  # Draw raindrop

        # Display human score
        score_human_text = font.render(f'Human Score: {score_human}', True, RED)
        screen.blit(score_human_text, (10, 10))

        # Display AI score
        score_ai_text = font.render(f'AI Score: {score_ai}', True, GREEN)
        screen.blit(score_ai_text, (WIDTH // 2 + 10, 10))

        # Display time remaining
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        time_text = font.render(f'Time: {game_duration - elapsed_time}', True, BLUE)
        screen.blit(time_text, (WIDTH - 120, 10))

        # Check game end condition
        if elapsed_time >= game_duration:
            if game_over_sound:
                game_over_sound.play()  # Play game over sound
            if show_game_over_screen():
                # Reset scores
                score_human = 0
                score_ai = 0
                return True  # Return to menu

        pygame.display.flip()
        clock.tick(FPS)

# Function to display start screen and select game mode
def show_start_screen():
    screen.fill(WHITE)
    start_text = large_font.render("Rain Bucket Game - Human vs. AI", True, BLUE)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(start_text, start_rect)

    start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
    pygame.draw.rect(screen, BLUE, start_button)
    start_button_text = font.render("Start Game", True, WHITE)
    start_button_text_rect = start_button_text.get_rect(center=start_button.center)
    screen.blit(start_button_text, start_button_text_rect)

    pygame.display.flip()

    # Wait for the player to click on start game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    return True

# Main game execution loop
while True:
    if show_start_screen():
        if game_loop_human_vs_ai(30):  # Set the game duration here (in seconds)
            continue  # Return to menu

pygame.quit()
sys.exit()
