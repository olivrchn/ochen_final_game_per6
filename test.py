import pygame
import random

# Set up game window
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up maze
maze_width = 20
maze_height = 15
maze = []
for row in range(maze_height):
    maze.append([])
    for column in range(maze_width):
        if random.random() < 0.3:
            maze[row].append(1)  # wall
        else:
            maze[row].append(0)  # path

# Set up sprites
player_image = pygame.image.load("steve.png")
player = pygame.sprite.Sprite()
player.image = player_image
player.rect = player.image.get_rect()
player.rect.x = 32
player.rect.y = 32
player_speed = 4

goal_image = pygame.Surface((32, 32))
goal_image.fill(red)
goal = pygame.sprite.Sprite()
goal.image = goal_image
goal.rect = goal.image.get_rect()
goal.rect.x = screen_width - 64
goal.rect.y = screen_height - 64

# Set up game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.rect.y -= player_speed
            elif event.key == pygame.K_DOWN:
                player.rect.y += player_speed
            elif event.key == pygame.K_LEFT:
                player.rect.x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player.rect.x += player_speed

    # Check for collision with walls
    for row in range(maze_height):
        for column in range(maze_width):
            if maze[row][column] == 1:
                wall_rect = pygame.Rect(column * 32, row * 32, 32, 32)
                if player.rect.colliderect(wall_rect):
                    player.rect = player.rect.move(-player_speed, -player_speed)

    # Check for collision with goal
    if player.rect.colliderect(goal.rect):
        game_over = True

    # Draw maze
    screen.fill(black)
    for row in range(maze_height):
        for column in range(maze_width):
            if maze[row][column] == 1:
                wall_rect = pygame.Rect(column * 32, row * 32, 32, 32)
                pygame.draw.rect(screen, white, wall_rect)
    pygame.draw.rect(screen, red, goal.rect)

    # Draw player
    screen.blit(player.image, player.rect)

    # Update display
    pygame.display.flip()

    # Set frame rate
    clock.tick(60)

# Game over
pygame.quit()