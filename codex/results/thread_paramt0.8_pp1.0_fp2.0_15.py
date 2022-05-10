import sys, threading
threading.Thread(target=lambda: sys.exit()).start()

import os
if os.name == "posix":
    os.kill(os.getpid(), 9)

import pygame
pygame.quit()

import time
print(time.time())
time.sleep(3)
