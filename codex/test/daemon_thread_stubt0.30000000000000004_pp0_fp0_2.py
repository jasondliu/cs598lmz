import sys, threading

def run():
    print("running")
    sys.stdout.flush()
    time.sleep(1)
    print("done")
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()
print("started")
sys.stdout.flush()
t.join()
print("joined")
sys.stdout.flush()
