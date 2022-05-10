import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)

threading.Thread(target=run).start()

