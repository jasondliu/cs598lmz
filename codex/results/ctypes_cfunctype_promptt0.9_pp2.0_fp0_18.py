import ctypes
# Test ctypes.CFUNCTYPE callbacks outside of pygame
# Does not work in 2.6 on Windows
# It prints "called" sporadically, instead of once per loop.
#

try:
    windll.winmm
except:
    raise SystemExit("Requires Windows")


import pygame

@pygame.sprite.Sprite.register
class EventSprite(pygame.sprite.Sprite):

    action = {}

    def __init__(self, evtname, **kwds):
        super(EventSprite, self).__init__(**kwds)
        self.evtname = evtname
        self.action[evtname] = 0

    def evt(self, source):
        self.action[self.evtname] += 1
        print(self.evtname, self.action[self.evtname], source)

def wm_key(wind, msg, wparam, lparam):
    print('key', wind, msg, wparam, lparam)
    return 0

def timer(id, msg, user, dw1, dw2
