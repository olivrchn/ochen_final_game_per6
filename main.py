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
from math import floor

# import settings 
from settings import *

# allow for a time stamp at the bottom
class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/10)
        self.delta = self.current_time - self.event_time
        # print(self.delta)
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/10)

# the class that the game is run upon
class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)

        # fill screen will PURPLE
        self.screen.fill(PURPLE)

        # load image of the main sprite
        self.image = pg.image.load('steve.jpg').convert_alpha()

        # resize the image to fit in the cell
        self.image = pg.transform.scale(self.image, (40, 40))

    def new(self):
        # start a new game
        self.x = 0
        self.y = 0
        self.game_gone = False
        
        # create Cooldown object
        self.cd = Cooldown()
        self.cd.timer()
        
        # use 2D array for the maze
        self.maze = [
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1], 
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1], 
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], 
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0], 
            [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0], 
            [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], 
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1], 
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], 
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        ]

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            # checks if key was pressed
            if event.type == pg.KEYDOWN:
                if self.inbounds(self.x, self.y, event) and self.collide(self.x, self.y, event):
                    if event.key == pg.K_LEFT:
                        self.x -= 40
                    elif event.key == pg.K_RIGHT:
                        self.x += 40
                    elif event.key == pg.K_UP:
                        self.y -= 40
                    elif event.key == pg.K_DOWN:
                        self.y += 40

    def update(self):
        # Game Loop - Update
        if self.x == WIDTH-40 and self.y == HEIGHT-40:
            self.game_gone = True
        
        # don't tick after game_gone
        if self.game_gone != True:
            self.cd.ticking()
        
    def draw(self):
        # check if reaching target spot
        if self.game_gone:
            self.game_over()
        else:
            # draw the maze
            for row in range(len(self.maze)):
                for col in range(len(self.maze[row])):
                    self.cell(row,col)
            self.grid()
            # Display the steve image
            self.screen.blit(self.image, (self.x, self.y))

        self.draw_text(str(self.cd.delta/100) + " seconds", 40, WHITE, 130, HEIGHT-60)

        # update the window
        pg.display.flip()

    # game over function
    def game_over(self):
        font = pg.font.Font(None, 90)

        # Set the game over message
        game_over_message = "You Win! Game Over!"

        # Render the game over message
        game_over_text = font.render(game_over_message, True, WHITE)

        # Get the size of the game over message
        game_over_text_size = game_over_text.get_size()

        # Calculate the position of the game over message
        game_over_text_pos = ((WINDOW[0]-game_over_text_size[0])/2, (WINDOW[1]-game_over_text_size[1])/2)

        # redraw the screen with black
        self.screen.fill(BLACK)

        # display the text on screen
        self.screen.blit(game_over_text, game_over_text_pos)

    # drawing the cell
    def cell(self, row, col):
        x = col * CELL_WIDTH
        y = row * CELL_HEIGHT
        # In self.maze, if a value is 1 the color is red
        if self.maze[row][col] == 1:
            color = RED
        elif self.maze[row][col] == 2:
            color = GREEN
        else:
            color = PURPLE
        # draw possible paths/walls on screen
        pg.draw.rect(self.screen, color, [x, y, CELL_WIDTH, CELL_HEIGHT])

    # draws a grid
    def grid(self):
        for x in range(0, WIDTH, CELL_WIDTH):
            for y in range(0, WIDTH, CELL_HEIGHT):
                rect = pg.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
                pg.draw.rect(self.screen, GRAY, rect, 1)

    # check inbounds
    def inbounds(self, x, y, event):
        if event.key == pg.K_LEFT:
            if x - 40 < 0 or x - 40 > WIDTH-40:
                return False
            else:
                return True
        elif event.key == pg.K_RIGHT:
            if x + 40 < 0 or x + 40 > WIDTH-40:
                return False
            else:
                return True
        elif event.key == pg.K_UP:
            if y - 40 < 0 or y - 40 > HEIGHT-40:
                return False
            else:
                return True
        elif event.key == pg.K_DOWN:
            if y + 40 < 0 or y + 40 > HEIGHT-40:
                return False 
            else:
                return True
        
    # check if colliding with wall
    def collide(self, x, y, event):
        if event.key == pg.K_LEFT:
            if self.maze[y//40][(x-40)//40] != 1:
                return False
            else:
                return True
        elif event.key == pg.K_RIGHT:
            if self.maze[y//40][(x+40)//40] != 1 :
                return False
            else:
                return True
        elif event.key == pg.K_UP:
            if self.maze[(y-40)//40][x//40] != 1:
                return False
            else:
                return True
        # since the player must go down in order to win, this is the only fuction with that cabability
        elif event.key == pg.K_DOWN:
            if self.maze[(y+40)//40][x//40] != 1 and self.maze[(y+40)//40][x//40] != 2:
                return False
            else:
                return True
 
    # draws the text once the game has been won.
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
while g.running:
    g.new()

pg.quit()