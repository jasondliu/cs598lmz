import sys, threading

def run():
    print("Running")
    sys.stdout.flush()
    threading.Timer(1, run).start()

run()
</code>

