import sys, threading

def run():
    while True:
        print(threading.current_thread().getName())
        sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

while True:
    print(threading.current_thread().getName())
    sys.stdout.flush()
