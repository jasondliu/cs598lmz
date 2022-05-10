import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Initialise Pygame
pygame.init()
# Open a new window
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.png")

# Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Game Over
over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change =
