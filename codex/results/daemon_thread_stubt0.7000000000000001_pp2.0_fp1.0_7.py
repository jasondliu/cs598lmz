import sys, threading

def run():
    sys.stdout.write("A")
    threading.Timer(1, run).start()

run()
</code>

