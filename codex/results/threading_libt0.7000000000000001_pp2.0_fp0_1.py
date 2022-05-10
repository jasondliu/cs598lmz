import threading
threading.stack_size(102400)

from pymouse import PyMouse
from pykeyboard import PyKeyboard

class Bot:
    def __init__(self):
        self.k = PyKeyboard()
        self.m = PyMouse()
        self.main()

    def main(self):
        self.m.move(self.m.screen_size()[0]/2, self.m.screen_size()[1]/2)
        self.m.click(self.m.screen_size()[0]/2, self.m.screen_size()[1]/2, 1)
        self.k.type_string("This is a test")
        self.k.press_key(self.k.enter_key)
        self.k.release_key(self.k.enter_key)
        self.k.tap_key(self.k.enter_key)



if __name__ == "__main__":
    b = Bot()
