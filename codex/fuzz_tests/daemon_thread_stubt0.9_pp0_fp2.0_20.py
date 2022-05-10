import sys, threading

def run():
    n = sys.argv[1]
    s = sys.argv[2]
    print('Timeout:', n, 'seconds')
    time.sleep(float(n))
    print('Exiting', s)


for s in map(str, range(10)):
    print('Starting thread')
    thread = threading.Thread(target=run, args=('0.2', s))
    thread.start()
