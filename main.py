# File created by: Oliver Chen
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes

# This file was created by: Oliver Chen
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg

# import settings 
from settings import *

# use 2D array for the maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# init pygame
pg.init()

# set the dimension of the screen that the maze will display on
screen = pg.display.set_mode((1200,800))

# set the name of the game window
pg.display.set_caption("Oliver's Maze")

# set the clock for the games frame rate
# clock = pg.time.Clock()

# set the fps
# clock.tick(FPS)

# drawing the cell
def cell(row, col):
    x = col * CELL_WIDTH
    y = row * CELL_HEIGHT
    if maze[row][col] == 1:
        color = GREEN
    else:
        color = RED
    # draw possible paths/walls on screen
    pg.draw.rect(screen, color, [x, y, CELL_WIDTH, CELL_HEIGHT])

# fill screen will color
screen.fill(PURPLE)

# load image of the main sprite
image = pg.image.load('steve.jpg').convert_alpha()

# resize the image to fit in the cell
image = pg.transform.scale(image, (40,40))

x = 0
y = 0
# this ensures main game loop will quit
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # draw the maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            cell(row,col)
    
    if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x -= 40
            elif event.key == pg.K_RIGHT:
                x += 40
            elif event.key == pg.K_UP:
                y -= 40
            elif event.key == pg.K_DOWN:
                y += 40

    # Display the steve image
    screen.blit(image, (x, y))

    # update the window
    pg.display.flip()

pg.quit()

        
