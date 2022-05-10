import sys, threading

def run():
    while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)

t = threading.Thread(target=run)
t.start()

while True:
    sys.stdout.write("o")
    sys.stdout.flush()
