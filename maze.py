import pygame
from config import CELL_SIZE, WHITE, BLACK
import random

def get_maze():
    # Define a simple maze layout (0 = empty space, 1 = wall)
    
    height = 60
    width = 120
    maze = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            maze[i][j] = random.choices([0, 1], weights=[70, 30])[0]
    print(maze)
    maze[0][0]=0
    return maze, height, width
    

def draw_maze(screen, maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = BLACK if cell == 1 else WHITE
            pygame.draw.rect(screen, color, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
