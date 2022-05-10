import sys, threading

def run():
    while True:
        sys.stdout.write("Hello world 2!\n")
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    sys.stdout.write("Hello world 1!\n")
    sys.stdout.flush()
    time.sleep(1)
