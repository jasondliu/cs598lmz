import sys, threading

def run():
    while True:
        print("Hello from thread %s" % threading.current_thread())
        sys.stdout.flush()

threading.Thread(target=run).start()
</code>

