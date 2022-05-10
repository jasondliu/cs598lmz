import sys, threading

def run():
    sys.stdout.write("Hello from Python %s\n" % (sys.version,))

threading.Thread(target=run).start()
</code>

