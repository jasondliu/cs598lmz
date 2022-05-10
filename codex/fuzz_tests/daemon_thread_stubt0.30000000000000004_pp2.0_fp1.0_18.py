import sys, threading

def run():
    sys.stdout.write('Thread started\n')
    sys.stdout.flush()
    time.sleep(2)
    sys.stdout.write('Thread finished\n')
    sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

sys.stdout.write('Main thread\n')
sys.stdout.flush()

thread.join()

sys.stdout.write('Main thread finished\n')
sys.stdout.flush()
