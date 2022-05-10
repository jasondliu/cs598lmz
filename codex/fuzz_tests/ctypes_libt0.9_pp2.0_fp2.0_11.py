import ctypes
ctypes.CDLL("libSDL2_image.so")
ctypes.CDLL("libSDL2.so")
#import helper # helper.py defines a variety of utilities
import sys



# os.environ['SDL_VIDEO_CENTERED'] = '1'
# Globals

PICS = [\
        ['myGirl.jpg', (18, 0)],\
        ['theCard.jpg', (432, 0)],\
        ['welcomeText.jpg', (0, 0)],\
        ['localFall.jpg', (0, 0)],\
        ['pumpkin.jpg', (0, 0)],\
        ['fall.jpg', (0, 0)]\
        ]

class State(object):
    def enter(self):
        raise NotImplementedError()
    def exit(self):
        return None
    def update(self, dt):
        raise NotImplementedError()
    def on_event(self, event):
        raise NotImplementedError()

class StateMachine(object):
    def __init__
