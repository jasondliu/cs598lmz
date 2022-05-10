import sys, threading

def run():
    while 1:
        sys.stdout.write(sys.stdin.readline())

threading.Thread(target=run).start()

while 1:
    sys.stdout.write(sys.stdout.readline())
</code>

