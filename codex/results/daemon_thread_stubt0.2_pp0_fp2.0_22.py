import sys, threading

def run():
    print("Thread started")
    sys.stdout.flush()
    time.sleep(5)
    print("Thread finished")
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

print("Main thread finished")
sys.stdout.flush()
</code>

