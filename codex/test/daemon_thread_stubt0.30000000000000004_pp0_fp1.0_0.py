import sys, threading

def run():
    print("hello")

t = threading.Thread(target=run)
t.start()

sys.exit(0)
