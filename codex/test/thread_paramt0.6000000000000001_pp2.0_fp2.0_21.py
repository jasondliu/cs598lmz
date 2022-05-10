import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()
#Thread 1
#Thread 2

#Multiple Threads
import threading
class MyThread(threading.Thread):
    def run(self):
        print('{} has started!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
t1 = MyThread(target=lambda: print('Hello from thread 1!'))
t2 = MyThread(target=lambda: print('Hello from thread 2!'))
t1.start(); t2.start()
#Thread-1 has started!
#Thread-2 has started!
#Hello from thread 1!
#Hello from thread 2!
