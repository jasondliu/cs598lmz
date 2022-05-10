import signal
signal.signal(signal.SIGINT, signal_handler)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], 0, 32)

playerH = 100
playerW = 15

pygame.display.set_caption('Pong')

white = (255, 255, 255)

p1_start_state = State(pos_h=SCREEN_HEIGHT / 2,
                       pos_w=playerW,
                       vel_h=0,
                       vel_w=0,
                       score=0
                       )
p2_start_state = State(pos_h=SCREEN_HEIGHT / 2,
                       pos_w=SCREEN_WIDTH - playerW,
                       vel_h=0,
                       vel_w=0,
                       score=0
                       )

