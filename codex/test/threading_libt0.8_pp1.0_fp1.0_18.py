import threading
threading.currentThread().setName("MainThread")

# start pygame
pygame.init()

#game variables
game_name = "Civilize"
game_icon = pygame.image.load("resources/logo.png")
pygame.display.set_icon(game_icon)
game_background = pygame.image.load("resources/background.png")
screen_width = 512
screen_height = 512
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Civilize")
FPS = 60
clock = pygame.time.Clock()

# button
green_button = pygame.image.load("resources/green_button.png")
blue_button = pygame.image.load("resources/blue_button.png")
red_button = pygame.image.load("resources/red_button.png")
green_button_rect = green_button.get_rect()
blue_button_rect = blue_button.get_rect()
