import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        # do some computation
        result = line.upper()
        # send the result
        sys.stdout.write(result)
        sys.stdout.flush()

worker = threading.Thread(target=run)
worker.setDaemon(True)
worker.start()

# send input to the running process
while True:
    d = sys.stdin.read(1)
    if not d:
        break
    sys.stdout.write(d)
    sys.stdout.flush()
</code>

