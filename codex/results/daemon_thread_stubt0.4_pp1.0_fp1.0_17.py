import sys, threading

def run():
    print("run")
    sys.stdout.flush()
    threading.Timer(1, run).start()

run()
