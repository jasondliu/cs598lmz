import sys, threading

def run():
    while True:
        print("hello")

t = threading.Thread(target=run)
t.start()

sys.exit()
