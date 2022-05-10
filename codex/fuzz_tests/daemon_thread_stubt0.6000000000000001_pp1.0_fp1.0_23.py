import sys, threading

def run():
    sys.stdout.write("Hello world\n")
    sys.stdout.flush()
    sys.stdout.write("Goodbye world\n")
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()
