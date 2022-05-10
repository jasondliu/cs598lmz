import sys, threading

def run():
    while True:
        sys.stdout.write(b'1')
        sys.stdout.flush()

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    pass
</code>

