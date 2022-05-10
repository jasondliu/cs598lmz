import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        return
    signal.setitimer(signal.ITIMER_REAL, 0)
    pygame.quit()
    sys.exit()

signal.signal(signal.SIGALRM, handler)

pygame.init()
screen = pygame.display.set_mode((400, 300))

handler()

while True:
    handler()
    screen.fill((0, 0, 0))
    pygame.display.flip()
