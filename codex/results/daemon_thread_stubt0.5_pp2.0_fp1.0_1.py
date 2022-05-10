import sys, threading

def run():
    sys.exit(0)

threading.Thread(target=run).start()

while True:
    pass
</code>

