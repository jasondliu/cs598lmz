import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect ro nothing
sqlite3.connect(":memory:")
print("Imports OK on {0} with {1}".format(os.name, ctypes.util.find_library("SDL2")))

import pygame
pygame.init()
#pygame.mixer.quit()
#pygame.display.init()
#pygame.font.init()
#pygame.joystick.quit()
#pygame.event.quit()
#pygame.image.quit()
#pygame.mixer.quit()
#pygame.quit()
pygame.fastevent.init()
print("Pygame SDL Initialization OK")

#if os.name == 'nt':
    #print("Setting SDL audio driver to dsound")
    #pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffersize=512)
    #pygame.display.set_mode((1,1))
#else:
#    print("Setting SDL audio driver to alsa")
#    os.environ["SDL_AUDIODR
