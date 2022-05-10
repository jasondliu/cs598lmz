import sys, threading

def run():
    while True:
        try:
            print(sys.stdin.readline().strip())
        except EOFError:
            break

threading.Thread(target=run).start()
</code>

