import sys, threading

def run():
    sys.exit(0)

thread = threading.Thread(target=run)
thread.start()
thread.join()
</code>

