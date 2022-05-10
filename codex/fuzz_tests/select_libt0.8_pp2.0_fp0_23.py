import select
import signal
import sys
import os

class InputHandler(object):
    '''
    Input event handler that notifies observers of user input.
    '''

    def __init__(self, on_input):
        self.on_input = on_input
        self.running = True
        signal.signal(signal.SIGINT, self.stop)

    def start(self):
        while self.running:
            i, o, e = select.select([sys.stdin], [], [], 1)
            if i:
                char = sys.stdin.read(1)
                self.on_input(char)

    def stop(self, x, y):
        self.running = False
        os._exit(0)
