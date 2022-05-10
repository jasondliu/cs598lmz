import _struct as st
import image

#==============================================================================

palette = [
    (  0,  0,  0), # black
    (255,255,255), # white
    (255,  0,  0), # red
    (  0,255,  0), # green
    (  0,  0,255), # blue
    (255,255,  0), # yellow
    (  0,255,255), # cyan
    (255,  0,255)  # magenta
]

#==============================================================================

class Rectangle(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.brightness = 1.0
    def move(self, dx, dy):
    	rect = Rectangle(self.x+dx, self.y+dy, self.w, self.h, self.color)
    	rect.brightness=self.brightness

