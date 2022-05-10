import sys, threading

def run():
    lock.acquire()
    print('Hello')
    sys.stdout.flush()
    lock.release()

lock = threading.Lock()
threading.Thread(target=run).start()
run()
