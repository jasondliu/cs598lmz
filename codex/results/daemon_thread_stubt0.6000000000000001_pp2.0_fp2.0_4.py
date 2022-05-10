import sys, threading

def run():
    sys.stdout.write("hello\n")
    sys.stdout.flush()
    sys.stdout.write("world\n")

thread = threading.Thread(target=run)
thread.start()
thread.join()
