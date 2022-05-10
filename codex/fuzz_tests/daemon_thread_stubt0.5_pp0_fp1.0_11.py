import sys, threading

def run():
    sys.exit(0)

thread = threading.Thread(target=run)
thread.start()

# This will raise an exception, because sys.exit() is called
# from another thread.
sys.exit(1)
</code>

