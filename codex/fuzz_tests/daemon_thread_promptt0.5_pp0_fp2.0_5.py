import threading
# Test threading daemon

class MyThread(threading.Thread):
    def run(self):
        print('{} has started!'.format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

def doubler(number):
    """
    A function that can be used by a thread
    """
    print(threading.currentThread().getName() + '\n')
    print(number)
    print()
    result = number * 2
    print("{} doubled to {}".format(number, result))
    print(threading.currentThread().getName() + '\n')

if __name__ == '__main__':
    for i in range(5):
        t = MyThread(target=doubler, name="thread" + str(i), args=(i,))
        # t.setDaemon(True)
        t.start()
        # t.join()

    print("done!")
