import sys, threading

def run():
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(10):
        print(i)

#threading.Thread(target=run, name='Thread-A').start()

#print('thread %s ended.' % threading.current_thread().name)


# create a sub class and override run function
# if run function is not be overrided, default run() function will be called
class MyThread(threading.Thread):
    def __init__(self, name, n):
        threading.Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        print('thread %s is running....' % threading.current_thread().name)
        for i in range(5):
            print(self.n)


t1 = MyThread('Thread-A', 1)
t2 = MyThread('Thread-B', 2)

t1.start()
t2.start()

t1.join()
t2.join()
