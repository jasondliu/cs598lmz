import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 560
CELL_WIDTH = WINDOW_WIDTH // 4
CELL_HEIGHT = (WINDOW_HEIGHT - 80) // 4

# 字体
BASICFONT = pygame.font.Font("FZY4JW.TTF", 60)
SMALLFONT = pygame.font.Font("FZY4JW.TTF", 30)

# 颜色
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 128, 0)
PURPLE
