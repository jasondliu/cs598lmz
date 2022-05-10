import sys, threading

def run():
    sys.stdout.write('Thread-2 is running\n')
    sys.stdout.flush()

threads = [threading.Thread(target=run) for i in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

sys.stdout.write('Thread-1 is running\n')
sys.stdout.flush()
