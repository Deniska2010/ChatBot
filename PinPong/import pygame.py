import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування ігрового поля
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

# Колір
BLACK = (0, 0, 0)
LINE_COLOR = (255, 255, 255)

# Розмір ігрової дошки
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

# Створення ігрової дошки
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Функція для малювання ігрової дошки
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            pygame.draw.rect(screen, LINE_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if board[row][col] == 'X':
                pygame.draw.line(screen, LINE_COLOR, (col * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), 2)
                pygame.draw.line(screen, LINE_COLOR, ((col + 1) * CELL_SIZE, row * CELL_SIZE), (col * CELL_SIZE, (row + 1) * CELL_SIZE), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, LINE_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2, 2)

# Головний цикл гри
turn = 'X'
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
    
    screen.fill(BLACK)
    draw_board()
    pygame.display.update()

    # Перевірка на перемогу
    for row in range(BOARD_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != '':
            game_over = True
        if board[0][row] == board[1][row] == board[2][row] != '':
            game_over = True
    if board[0][0] == board[1][1] == board[2][2] != '':
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] != '':
        game_over = True

# Очікування завершення гри
pygame.time.wait(3000)
pygame.quit()
sys.exit()
