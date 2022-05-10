import sys, threading

def run():
    while True:
        print(threading.currentThread().getName())
        sys.stdout.flush()

threading.Thread(target=run).start()
threading.Thread(target=run).start()
