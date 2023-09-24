import pygame
from pygame.locals import *

# Ініціалізація Pygame
pygame.init()

# Встановлення розміру вікна гри
WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pin Pong")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметри ракеток
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5

# Параметри м'яча
BALL_RADIUS = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Початкові координати ракеток та м'яча
paddle1_x = 0
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_x = WIDTH - PADDLE_WIDTH
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Швидкість ракеток
paddle1_vel = 0
paddle2_vel = 0

# Шрифт для відображення рахунку
font = pygame.font.Font(None, 36)

def update():
    global paddle1_y, paddle2_y, ball_x, ball_y, paddle1_vel, paddle2_vel
    
    # Оновлення позицій ракеток та м'яча
    paddle1_y += paddle1_vel
    paddle2_y += paddle2_vel
    ball_x += BALL_SPEED_X
    ball_y += BALL_SPEED_Y
    
    # Відскок м'яча від верхньої та нижньої границі
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        BALL_SPEED_Y *= -1
    
    # Відскок м'яча від ракеток
    if ball_x - BALL_RADIUS <= PADDLE_WIDTH and paddle1_y - BALL_RADIUS <= ball_y <= paddle1_y + PADDLE_HEIGHT + BALL_RADIUS:
        BALL_SPEED_X *= -1
    elif ball_x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and paddle2_y - BALL_RADIUS <= ball_y <= paddle2_y + PADDLE_HEIGHT + BALL_RADIUS:
        BALL_SPEED_X *= -1
    
    # Перевірка на завершення гри
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        # Здійснюємо підрахунок очків
        if ball_x - BALL_RADIUS <= 0:
            score2 += 1
        else:
            score1 += 1
        
        # Повертаємо м'яч в центр
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        BALL_SPEED_X *= -1

    # Оновлення вікна
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(win, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.update()

# Основний цикл гри
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_w:
                paddle1_vel = -PADDLE_SPEED
            elif event.key == K_s:
                paddle1_vel = PADDLE_SPEED
            elif event.key == K_UP:
                paddle2_vel = -PADDLE_SPEED
            elif event.key == K_DOWN:
                paddle2_vel = PADDLE_SPEED
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                paddle1_vel = 0
            elif event.key == K_UP or event.key == K_DOWN:
                paddle2_vel = 0
    
    update()
    clock.tick(60)

pygame.quit()
