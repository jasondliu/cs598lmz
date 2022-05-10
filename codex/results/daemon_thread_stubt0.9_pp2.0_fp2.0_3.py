import sys, threading

def run():
    sys.exit(0)

t = threading.Thread(target=run)
t.start()
t.join()
