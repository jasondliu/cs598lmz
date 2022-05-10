import sys, threading

def run():
    print("hello")
    sys.stdout.flush()

threading.Thread(target=run).start()
</code>

