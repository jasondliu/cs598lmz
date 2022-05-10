import sys, threading

def run():
    print("Thread started")
    sys.stdout.flush()
    time.sleep(2)
    print("Thread finished")
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

print("Main thread")
sys.stdout.flush()
</code>
Output:
<code>Main thread
Thread started
Thread finished
</code>

