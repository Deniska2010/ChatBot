import pygame
import random

pygame.init()


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


BLOCK_SIZE = 20
SNAKE_SIZE = BLOCK_SIZE
FRUIT_SIZE = BLOCK_SIZE


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змійка")


def message(msg, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [x, y])


def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])


def game():
    game_over = False
    game_close = False


    lead_x = SCREEN_WIDTH / 2
    lead_y = SCREEN_HEIGHT / 2


    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1


    fruit_x = round(random.randrange(0, SCREEN_WIDTH - FRUIT_SIZE) / FRUIT_SIZE) * FRUIT_SIZE
    fruit_y = round(random.randrange(0, SCREEN_HEIGHT - FRUIT_SIZE) / FRUIT_SIZE) * FRUIT_SIZE

    clock = pygame.time.Clock()
    snake_speed = 10

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message("Ви програли! Натисніть Q для виходу або С для заново", RED, 30, 200, 250)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0

        if lead_x >= SCREEN_WIDTH or lead_x < 0 or lead_y >= SCREEN_HEIGHT or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [fruit_x, fruit_y, FRUIT_SIZE, FRUIT_SIZE])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        if lead_x == fruit_x and lead_y == fruit_y:
            fruit_x = round(random.randrange(0, SCREEN_WIDTH - FRUIT_SIZE) / FRUIT_SIZE) * FRUIT_SIZE
            fruit_y = round(random.randrange(0, SCREEN_HEIGHT - FRUIT_SIZE) / FRUIT_SIZE) * FRUIT_SIZE
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game()