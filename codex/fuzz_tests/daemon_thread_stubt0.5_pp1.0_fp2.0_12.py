import sys, threading

def run():
    print("thread")
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

print("main")
sys.stdout.flush()

t.join()
</code>

