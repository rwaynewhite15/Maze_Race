import pygame
from config import CELL_SIZE, GREEN

class Player:
    def __init__(self, start_pos, maze):
        self.position = start_pos
        self.maze = maze
        self.color = (0, 0, 255)  # Blue color for the player

    def move(self, direction):
        x, y = self.position
        if direction == "UP" and y > 0 and self.maze[y - 1][x] == 0:
            self.position = (x, y - 1)
        elif direction == "DOWN" and y < len(self.maze) - 1 and self.maze[y + 1][x] == 0:
            self.position = (x, y + 1)
        elif direction == "LEFT" and x > 0 and self.maze[y][x - 1] == 0:
            self.position = (x - 1, y)
        elif direction == "RIGHT" and x < len(self.maze[0]) - 1 and self.maze[y][x + 1] == 0:
            self.position = (x + 1, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
