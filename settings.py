WIDTH = 1300
HEIGHT = 900
PLAYER_ACC = 2
PLAYER_FRICTION = -1
PLAYER_GRAV = 0
MOB_ACC = 2
MOB_FRICTION = -0.3
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
GREEN = (50,255,0)
FPS = 120
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 30, WIDTH, 40, (200,200,200), "normal"),
                 (0, 0, WIDTH, 40, (200,200,200), "normal"),
                 (0, 0, 40, HEIGHT, (200,200,200), "normal"),
                 (WIDTH-40, 0, 40, HEIGHT, (200,200,200), "normal")]
#                (x, y, width, height, color, variant)