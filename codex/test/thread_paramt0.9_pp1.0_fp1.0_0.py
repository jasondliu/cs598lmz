import sys, threading
threading.Thread(target=lambda: sys.stdout.write('X' * 100000000)).start()

from hx711 import HX711
from scale import Scale
from sqlite3 import connect


# def cleanAndExit():
#     print "Cleaning..."
#     GPIO.cleanup()
#     print "Bye!"
#     sys.exit()

# Clean GPIO on exit
# atexit.register(cleanAndExit)

