import threading
# Test threading daemon
import time


def worker(n):
    time.sleep(1)
    print('Worker {}'.format(n))

if __name__ == '__main__':
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
