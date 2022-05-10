import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Tom and Jerry")
# plays sound
import playsound
playsound.playsound('tom and jerry.mp3', True)

# initialize pygame
pygame.init()

# set screen
screen = pygame.display.set_mode((800, 580))

# title and icon
pygame.display.set_caption("Tom and Jerry")
pygame.display.set_icon(pygame.image.load('tom.png'))

# background
background = pygame.image.load('bg1.png')

# Jerry
jerryImg = pygame.image.load('jerry.png')
jerryX = 370
jerryY = 500
jerryXChange = 0

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Tom
tomImg = []
