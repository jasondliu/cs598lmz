import sys, threading

def run():
    while True:
        try:
            print(sys.stdin.readline())
        except KeyboardInterrupt:
            break

thread = threading.Thread(target=run)
thread.start()

while True:
    try:
        print(sys.stdin.readline())
    except KeyboardInterrupt:
        break
</code>

