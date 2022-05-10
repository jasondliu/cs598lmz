import sys, threading

def run():
    global stop
    sys.stdout.write('\n')
    sys.stdout.flush()
    while True:
        if stop:
            return
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)

stop = False
thread = threading.Thread(target=run)
thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop = True
    thread.join()
    print('\nStopped!')
