import pygame
import sys
import time
import random
from maze import draw_maze, get_maze
from snake import Snake
from player import Player
from pathfinding import a_star_search
from config import WIDTH, HEIGHT, CELL_SIZE, WHITE, BLACK, GREEN

def get_random_goal(maze):
    while True:
        x = random.randint(0, len(maze[0]) - 1)
        y = random.randint(0, len(maze) - 1)
        if maze[y][x] == 0:
            return (x, y)
def get_random_start(maze):
        # Generate a random start point within the maze, avoiding walls
        while True:
            x = random.randint(1, len(maze[0]) - 1)
            y = random.randint(1, len(maze) - 1)
            if maze[y][x] == 0:
                return (x, y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Maze Game')
    clock = pygame.time.Clock()

    maze, height, width = get_maze()

    # Create player
    player_start = get_random_start(maze)
    player = Player(player_start, maze)

    # Create multiple Snake instances
    snakes = []
    num_snakes = 1  # Number of snakes to create
    # goal = (random.randint(width // 4, width - 1), random.randint(height // 4, height - 1))
    goal = get_random_goal(maze)  # Initial goal
    for _ in range(num_snakes):
        start = player_start  # Start can be None to randomize or specify a fixed point
        snake = Snake(maze, start)
        # Define random goal points for each snake
        path = a_star_search(snake.current_pos, goal, maze)
        snake.set_path(path)
        snakes.append(snake)
    
    
    goal_reached = False

    player_score = 0
    computer_score = 0

    # Initialize the snake's position at the start of the path
    snake_pos = list(path)
    path_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Get the state of all keyboard buttons
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move("UP")
        if keys[pygame.K_DOWN]:
            player.move("DOWN")
        if keys[pygame.K_LEFT]:
            player.move("LEFT")
        if keys[pygame.K_RIGHT]:
            player.move("RIGHT")

        # Check if the player or any snake has reached the goal
        player_reached_goal = player.position == goal
        snakes_reached_goal = any(snake.current_pos == goal for snake in snakes)

        if player_reached_goal:
            player_score += 1
            goal_reached = True
        elif snakes_reached_goal:
            computer_score += 1
            goal_reached = True

        if goal_reached:
            # Move the goal to a new random position
            goal = get_random_goal(maze)
            goal_reached = False
            # Recalculate the path for each snake
            for snake in snakes:
                path = a_star_search(snake.current_pos, goal, maze)
                snake.set_path(path)

        screen.fill(WHITE)
        draw_maze(screen, maze)

        # Move and draw each snake
        for snake in snakes:
            snake.move_step()
            snake.draw(screen)

        # Draw the player
        player.draw(screen)

        # Draw the goal
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(goal[0] * CELL_SIZE, goal[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Display scores
        font = pygame.font.SysFont(None, 36)
        score_text = f"Player Score: {player_score} | Computer Score: {computer_score}"
        score_surface = font.render(score_text, True, (0, 0, 0))
        screen.blit(score_surface, (10, 10))

        pygame.display.flip()
        time.sleep(0.2)  # Control the speed of the snake

        clock.tick(60)

if __name__ == "__main__":
    main()