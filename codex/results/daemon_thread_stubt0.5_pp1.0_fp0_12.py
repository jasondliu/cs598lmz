import sys, threading

def run():
    while True:
        sys.stdout.write("a")
        sys.stdout.flush()

threading.Thread(target=run).start()

while True:
    sys.stdout.write("b")
    sys.stdout.flush()
