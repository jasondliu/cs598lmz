import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(1)
    print('End')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    d.start()
    print('d.isAlive()', d.isAlive())
    d.join(2)
    print('d.isAlive()', d.isAlive())
    print('Main thread end')


# Test threading lock
import threading, multiprocessing
def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# print('CPU number:', multiprocessing.cpu_count())
# print('thread number:', threading.activeCount())
# print('thread list:', threading.enumerate())
