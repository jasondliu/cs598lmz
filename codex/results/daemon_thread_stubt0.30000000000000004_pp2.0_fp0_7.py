import sys, threading

def run():
    sys.stdout.write('\n')
    sys.stdout.flush()
    sys.exit(0)

threading.Timer(0.5, run).start()

while True:
    sys.stdout.write('\r' + ' ' * 100)
    sys.stdout.flush()
    sys.stdout.write('\r' + '-' * 100)
    sys.stdout.flush()
    sys.stdout.write('\r' + ' ' * 100)
    sys.stdout.flush()
    sys.stdout.write('\r' + '-' * 100)
    sys.stdout.flush()
</code>

