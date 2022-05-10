import gc, weakref
from pynput import keyboard
import time

class KeyListener:
    def __init__(self):
        self.keys = []
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        self.keys.append(key)

    def on_release(self, key):
        self.keys.remove(key)

    def get_keys(self):
        return self.keys

    def get_keys_string(self):
        return "".join(str(x) for x in self.keys)

    def clear_keys(self):
        self.keys.clear()

class Game:
    def __init__(self):
        self.window = sdl2.ext.Window("Game", size=(800, 600))
        self.window.show()

        self.renderer = sdl2.ext.Renderer(self.window)
        self.renderer.blendmode = sdl2.
