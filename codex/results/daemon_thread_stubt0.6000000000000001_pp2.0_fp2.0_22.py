import sys, threading

def run():
    while True:
        input()
        sys.stdout.write('#')
        sys.stdout.flush()

threading.Thread(target=run).start()

while True:
    sys.stdout.write('.')
    sys.stdout.flush()
