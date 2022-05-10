import threading
# Test threading daemon
class MyThread(threading.Thread):
    def run(self):
        print('{} has started!'.format(self.getName()))
        time.sleep(1)
        print('{} has finished'.format(self.getName()))

if __name__ == '__main__':
    for x in range(4):
        mythread = MyThread(name = 'Thread-{}'.format(x + 1))
        mythread.setDaemon(True)
        mythread.start()
    print('Main thread has finished')

# Test multiprocessing
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

# Test multiprocessing from multiprocessing import Pool
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5
