import pygame
import random

pygame.init()

# Параметри гри
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 25
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Форми тетроміно
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 1, 1], [0, 1, 0]]
]

# Кольори для форм
SHAPE_COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (128, 0, 128)
]

# Ініціалізація вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Клас для представлення тетроміно
class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(SHAPE_COLORS)
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

# Ініціалізація гри
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_tetromino = Tetromino(random.choice(SHAPES))
clock = pygame.time.Clock()

# Основний цикл гри
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_tetromino.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                current_tetromino.move(1, 0)
            elif event.key == pygame.K_DOWN:
                current_tetromino.move(0, 1)
            elif event.key == pygame.K_UP:
                current_tetromino.rotate()

    # Рух тетроміно вниз
    if current_tetromino.y + len(current_tetromino.shape) < GRID_HEIGHT:
        current_tetromino.move(0, 1)

    # Оновлення сітки тетроміно
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] = 0

    for y, row in enumerate(current_tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[current_tetromino.y + y][current_tetromino.x + x] = current_tetromino.color

    # Відображення гри
    screen.fill(BLACK)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()