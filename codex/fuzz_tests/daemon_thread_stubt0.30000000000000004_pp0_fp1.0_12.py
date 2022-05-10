import sys, threading

def run():
    sys.stdout.write('\n')
    sys.stdout.flush()
    sys.exit(0)

timer = threading.Timer(2.0, run)
timer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    timer.cancel()
    sys.stdout.write('\n')
    sys.stdout.flush()
    sys.exit(0)
</code>

