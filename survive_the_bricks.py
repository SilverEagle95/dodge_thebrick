import pygame
import sys
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Bricks")
clock = pygame.time.Clock()


player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_visible = True
invulnerable_duration = 2.0
invulnerable_timer = 0.0


player_points = [(player_x, player_y), (player_x + player_size, player_y),
                 (player_x + player_size // 2, player_y - player_size)]


brick_width = 100
brick_height = 20
brick_speed = 5
bricks = []


score = 0
high_score = 0


font = pygame.font.Font(None, 36)


def draw_player():
    if player_visible:
        pygame.draw.polygon(screen, WHITE, player_points)


def draw_brick(x, y):
    pygame.draw.rect(screen, RED, (x, y, brick_width, brick_height))


def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))


def show_restart_button():
    restart_text = font.render("Click to Restart", True, WHITE)
    button_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(restart_text, button_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN and (score == 0 or time.time() > invulnerable_timer):
            score = 0
            bricks = []
            player_visible = True
            invulnerable_timer = time.time() + invulnerable_duration


    mouse_x, mouse_y = pygame.mouse.get_pos()


    player_x = mouse_x - player_size // 2
    player_points = [(player_x, player_y), (player_x + player_size, player_y),
                     (player_x + player_size // 2, player_y - player_size)]


    if random.randint(1, 100) < 5:
        brick_x = random.randint(0, WIDTH - brick_width)
        brick_y = -brick_height
        bricks.append((brick_x, brick_y))


    new_bricks = []
    for brick in bricks:
        brick_x, brick_y = brick
        brick_y += brick_speed
        if brick_y < HEIGHT:
            new_bricks.append((brick_x, brick_y))
        else:
            score += 1
    bricks = new_bricks


    high_score = max(high_score, score)


    if player_visible and time.time() > invulnerable_timer:
        for brick in bricks:
            brick_x, brick_y = brick
            if (
                player_x < brick_x < player_x + player_size or
                player_x < brick_x + brick_width < player_x + player_size
            ) and (
                player_y - player_size < brick_y < player_y or
                player_y - player_size < brick_y + brick_height < player_y
            ):
                score = 0
                player_visible = False
                invulnerable_timer = time.time() + invulnerable_duration


    screen.fill((0, 0, 0))


    draw_player()
    for brick in bricks:
        draw_brick(*brick)


    show_score()


    if (score == 0 or time.time() > invulnerable_timer) and not player_visible:
        show_restart_button()

    pygame.display.flip()

    clock.tick(FPS)
