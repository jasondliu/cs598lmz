import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

from common import keys, wait, config
from common.common import eprint
from time import sleep
from collections import defaultdict
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from common.game_canvas import GameCanvas

class InputCapture:
    def __init__(self, capture_mouse, capture_keyboard, send_function):
        self.capture_mouse = capture_mouse
        self.capture_keyboard = capture_keyboard
        self.send_function = send_function
        self.keyboard_buffer = []
        self.mouse_buffer = []

        canvas_thread = threading.Thread(target=self.run)
        canvas_thread.daemon = True
        canvas_thread.start()
        self.game_canvas_init()

        config.load()

    def game_canvas_init(self):
        self.game_canvas = GameCanvas()

