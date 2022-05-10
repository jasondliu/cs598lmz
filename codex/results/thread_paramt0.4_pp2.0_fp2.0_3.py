import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

led = board.get_pin('d:13:o')

while True:
    led.write(1)
    time.sleep(1)
    led.write(0)
    time.sleep(1)
