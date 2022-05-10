import sys, threading

def run():
    while True:
        print(threading.current_thread().getName())
        sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

while True:
    print(threading.current_thread().getName())
    sys.stdout.flush()
