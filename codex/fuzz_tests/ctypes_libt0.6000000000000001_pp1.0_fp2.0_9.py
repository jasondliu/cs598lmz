import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("FPS Counter")

pygame.init()

# Set display size
size = width, height = 1920,1080
screen = pygame.display.set_mode(size)

# Set background image
bg = pygame.image.load("bg.png")

# Set display caption
pygame.display.set_caption("FPS Counter")

# Set window icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Set FPS
clock = pygame.time.Clock()
FPS = 60

# Fonts
font_size = 40
font_size_small = 20

font_name = pygame.font.match_font("arial")
font_name_small = pygame.font.match_font("arial")

# Load font
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,
