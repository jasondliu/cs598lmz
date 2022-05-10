import sys, threading

def run():
    while True:
        print("Hello")
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    print("World")
    sys.stdout.flush()
    time.sleep(1)
</code>

