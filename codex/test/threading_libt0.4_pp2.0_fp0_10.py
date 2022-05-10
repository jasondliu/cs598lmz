import threading
threading.Thread(target=lambda: None).start()

import time
time.sleep(1)

from pynput.keyboard import Key, Controller
keyboard = Controller()

#Presses the 'a' key
keyboard.press('a')
keyboard.release('a')

#Presses the 'b' key
keyboard.press('b')
keyboard.release('b')

#Presses the 'c' key
keyboard.press('c')
keyboard.release('c')

#Presses the 'd' key
keyboard.press('d')
keyboard.release('d')

#Presses the 'e' key
keyboard.press('e')
keyboard.release('e')

#Presses the 'f' key
keyboard.press('f')
keyboard.release('f')

#Presses the 'g' key
keyboard.press('g')
keyboard.release('g')

#Presses the 'h' key
keyboard.press('h')
keyboard.release('h')

