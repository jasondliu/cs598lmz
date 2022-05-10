import sys, threading

def run():
    while True:
        print("hello")
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=run)
t.start();
</code>

