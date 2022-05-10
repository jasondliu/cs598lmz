import sys, threading

def run():
    sys.stdout.write("{}".format("Hello World"))

thread = threading.Thread(target=run)
thread.start()
</code>

