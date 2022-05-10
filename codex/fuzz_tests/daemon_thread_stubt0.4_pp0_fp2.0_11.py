import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(line)

threading.Thread(target=run).start()
</code>

