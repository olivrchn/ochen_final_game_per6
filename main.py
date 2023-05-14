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
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1], 
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1], 
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1], 
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0], 
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0], 
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
]

# check inbounds
def inbounds(x, y, event):
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
    
# check if colliding with red recd
def collide(x, y, event):
    if event.key == pg.K_LEFT:
        if maze[y//40][(x-40)//40] != 1:
            return False
        else:
            return True
    elif event.key == pg.K_RIGHT:
        if maze[y//40][(x+40)//40] != 1:
            return False
        else:
            return True
    elif event.key == pg.K_UP:
        if maze[(y-40)//40][x//40] != 1:
            return False
        else:
            return True
    elif event.key == pg.K_DOWN:
        if maze[(y+40)//40][x//40] != 1:
            return False
        else:
            return True




class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

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
                if inbounds(self.x, self.y, event) and collide(self.x, self.y, event):
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
        
    def draw(self):
        # check if reaching target spot
        if self.game_gone:
            self.game_over()
        else:
            # draw the maze
            for row in range(len(maze)):
                for col in range(len(maze[row])):
                    self.cell(row,col)
            # Display the steve image
            self.screen.blit(self.image, (self.x, self.y))

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
        if maze[row][col] == 1:
            color = GREEN
        else:
            color = RED
        # draw possible paths/walls on screen
        pg.draw.rect(self.screen, color, [x, y, CELL_WIDTH, CELL_HEIGHT])
 
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