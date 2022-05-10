import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

# To get the same results with every run
np.random.seed(1)
# To plot pretty figures
