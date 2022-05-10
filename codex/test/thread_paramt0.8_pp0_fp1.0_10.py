import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# This line is only for repl.it
sys.stdout.flush()

from time import sleep
import copy


def update():
    # This line is only for repl.it
    sys.stdout.flush()
    display.display(current_frame)
    sleep(1/10)


class Frame:
    def __init__(self, display_width=32, display_height=32):
        self.width = display_width
        self.height = display_height

        self.pixels = [
            [0 for x in range(display_width)]
            for y in range(display_height)
        ]

    def get_pixel(self, x, y):
        return self.pixels[y][x]

    def set_pixel(self, x, y, value):
        self.pixels[y][x] = value

    def copy(self):
        return copy.deepcopy(self)


current_frame = Frame()
