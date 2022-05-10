import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

# The following is a helper function 
# that I will use below. 
# Feel free to disregard this.
