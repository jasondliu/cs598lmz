import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Set up some colors
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
LIGHTRED = (175, 20, 20)
GREEN = (0, 155, 0)
LIGHTGREEN = (20, 175, 20)
BLUE = (0, 0, 155)
LIGHTBLUE = (20, 20, 175)
YELLOW = (155, 155, 0)
LIGHTYELLOW = (175, 175, 20)

# Set up some fonts
BASICFONT = pygame.font.Font('freesansbold.ttf', 32)
SMALLFONT = pygame.font.Font('freesansbold.ttf', 16)

# Set up some constants
SCREENWIDTH = 800
SCREENHEIGHT = 600

# Set up some variables
FPS = 60
clock = pygame.time.Clock()
