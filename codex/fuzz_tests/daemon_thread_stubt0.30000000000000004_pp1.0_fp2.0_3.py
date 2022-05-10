import sys, threading

def run():
    print("run")
    sys.exit(0)

threading.Thread(target=run).start()

print("main")
</code>
In this case, the <code>run</code> function is executed on a separate thread, but the <code>sys.exit</code> call does not terminate the main thread.
I'm using Python 3.5.2.

