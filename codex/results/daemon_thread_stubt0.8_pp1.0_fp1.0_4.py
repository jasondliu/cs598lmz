import sys, threading

def run():
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('Pygame-Demo')

    white = 255, 255, 255
    black = 20, 20, 40
    screen.fill(white)

    gameover = False

    paddle1 = pygame.Rect(1, 1, 20, 100)
    paddle2 = pygame.Rect(WINWIDTH - 20, 1, 20, 100)
    ball = pygame.Rect(WINWIDTH / 2, WINHEIGHT / 2, 15, 15)

    paddle1move = 0
    paddle2move = 0

    speed = 5

    bg = pygame.image.load("background.jpg").convert()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    paddle2move = -speed
                if event.key == K_DOWN:
                    paddle2move
