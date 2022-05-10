import sys, threading

def run():
    sys.stdout.write("Hello from Python %s\n" % (sys.version,))

thread = threading.Thread(target=run)
thread.start()
