import sys, threading
threading.Thread(target=lambda: sys.stdout.write(open('out.html', 'r').read()), daemon=True).start()

import itertools
from decimal import *
getcontext().prec = 14

DELTA = 0.001

class Path(object):

    def __init__(self):
        if self.__class__ == Path:
            raise Exception("Class 'Path' cannot be instantiated.")
        
        self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.new_subpath = True

    def up(self):
        self.move(  0, -DELTA)

    def down(self):
        self.move(  0, DELTA)

    def left(self):
        self.move(-DELTA, 0)

    def right(self):
        self.move(DELTA, 0)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.action(self, 'M', self.x, self.y)
