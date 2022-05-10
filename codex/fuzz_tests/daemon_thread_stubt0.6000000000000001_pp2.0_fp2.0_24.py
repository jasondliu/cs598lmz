import sys, threading

def run():
    for i in range(0, 100):
        print('Hello, world!')
    sys.exit(1)

t = threading.Thread(target=run)
t.start()
t.join()
