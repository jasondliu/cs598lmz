import sys, threading

def run():
    while(1):
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

while True:
    time.sleep(1)
    sys.stdout.write("o")
    sys.stdout.flush()
