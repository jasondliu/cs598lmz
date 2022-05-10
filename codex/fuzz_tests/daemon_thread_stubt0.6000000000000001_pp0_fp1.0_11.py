import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        print('T1:', line)

threading.Thread(target=run).start()
</code>

