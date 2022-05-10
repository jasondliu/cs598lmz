import sys, threading
threading.Thread(target=lambda: m.moveto(0, 0), args=[]).start() # do not wait for this task
