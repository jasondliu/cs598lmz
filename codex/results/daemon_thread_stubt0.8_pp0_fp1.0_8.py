import sys, threading

def run():
    lock = threading.Lock()
    with lock:
        print('in lock')
        sys.exit()
        print('out lock')
        with lock:
            print('in lock again')

t = threading.Thread(target=run)
t.start()
