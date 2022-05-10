import sys, threading

def run():
    sys.stdout.write("Hello from Python!\n")
    sys.stdout.flush()
    sys.exit(0)

thread = threading.Thread(target=run)
thread.start()
