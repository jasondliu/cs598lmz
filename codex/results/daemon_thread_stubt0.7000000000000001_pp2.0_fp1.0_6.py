import sys, threading

def run():
    print("starting")
    sys.stdout.flush()

    while True:
        pass

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

time.sleep(2)

print("stopping")
sys.stdout.flush()

thread.join()
</code>

