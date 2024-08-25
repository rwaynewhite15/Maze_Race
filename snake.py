import random
import pygame
from config import CELL_SIZE, GREEN

class Snake:
    def __init__(self, maze, start=None):
        self.maze = maze
        self.path = []
        self.path_index = 0
        
        # Random start point if not provided
        if start is None:
            self.start = self._get_random_start()
        else:
            self.start = start
        
        # Initialize snake's path
        self.current_pos = self.start
        self.path = [self.current_pos]

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def _get_random_start(self):
        # Generate a random start point within the maze, avoiding walls
        while True:
            x = random.randint(1, len(self.maze[0]) - 1)
            y = random.randint(1, len(self.maze) - 1)
            if self.maze[y][x] == 0:
                return (x, y)
    
    def set_path(self, path):
        self.path = path
        self.path_index = 0
        self.current_pos = self.path[self.path_index]
    
    def move_step(self):
        if self.path and self.path_index < len(self.path):
            # Occasionally choose a random move instead of following the path
            if random.random() < 0:  # 75% chance of a random move
                next_pos = (self.current_pos[0] + random.choice([-1, 1]), self.current_pos[1] + random.choice([-1, 1]))
                if 0 <= next_pos[0] < len(self.maze[0]) and 0 <= next_pos[1] < len(self.maze) and self.maze[next_pos[1]][next_pos[0]] == 0:
                    self.current_pos = next_pos
            else:
                next_pos = self.path[self.path_index]
                self.current_pos = next_pos
                self.path_index += 1
        
    def draw(self, screen):
        # Draw the snake as a series of green squares
        for pos in self.path[:self.path_index + 1]:
            pygame.draw.rect(screen, self.color, pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
