import sys, threading

def run():
    export_fn(export_val)

t = threading.Thread(target = run)
t.start()
t.join()

sys.exit(0)
