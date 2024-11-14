
import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Pengaturan layar
screen_size = 600
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Tic-Tac-Toe')

# Load gambar background
background_image = pygame.image.load('yyfgybdgf.jpg').convert()  # Ganti dengan path file gambar

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Inisialisasi musik latar
pygame.mixer.music.load('bensound-fiddlesticks.mp3')  # Ganti dengan path file musik
pygame.mixer.music.play(-1)  # Ulangi musik tanpa henti

# Variabel game
grid = [['' for _ in range(3)] for _ in range(3)]
current_player = 'S'
font = pygame.font.SysFont(None, 200)

# Fungsi untuk menggambar grid
def draw_board():
    screen.blit(background_image, (0, 0))  # Blit background image
    for row in range(1, 3):
        pygame.draw.line(screen, black, (0, row * screen_size // 3), (screen_size, row * screen_size // 3), 5)
        pygame.draw.line(screen, black, (row * screen_size // 3, 0), (row * screen_size // 3, screen_size), 5)

    for row in range(3):
        for col in range(3):
            if grid[row][col] != '':
                text = font.render(grid[row][col], True, red if grid[row][col] == 'X' else blue)
                screen.blit(text, (col * screen_size // 3 + 50, row * screen_size // 3 + 50))

# Fungsi untuk memeriksa kemenangan
def check_winner():
    for row in grid:
        if row[0] == row[1] == row[2] != '':
            return row[0]

    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != '':
            return grid[0][col]

    if grid[0][0] == grid[1][1] == grid[2][2] != '':
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0] != '':
        return grid[0][2]

    return None

# Game loop
running = True
winner = None

while running:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
            x, y = event.pos
            col = x // (screen_size // 3)
            row = y // (screen_size // 3)
            if grid[row][col] == '':
                grid[row][col] = current_player
                winner = check_winner()
                current_player = 'O' if current_player == 'S' else 'S'

    if winner is not None:
        print(f'Pemenang: {winner}')
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()

pygame.quit()