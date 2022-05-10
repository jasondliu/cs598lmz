import sys, threading

def run():
    print("running")
    sys.stdout.flush()
    while True:
        c = sys.stdin.read(1)
        print("got:", c)
        sys.stdout.flush()

t = threading.Thread(target=run)
t.daemon = True
t.start()

sys.stdout.flush()
while True:
    time.sleep(1)
</code>

