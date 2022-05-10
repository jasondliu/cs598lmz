import threading
threading.currentThread()
threading.activeCount()
threading.enumerate()
threading.main_thread()

#一般形式
class mythread(threading.Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n
    def run(self):
        print("This is num:%s"%self.n)

t1 = mythread("1")
t1.start()

#守护线程
t2 = mythread('2')
t2.setDaemon(True)
t2.start()

#信号量
sem = threading.Semaphore(3)
sem.acquire()
sem.release()

#事件
event = threading.Event()
event.set()
event.clear()
event.isSet()

#条件变量
mutex = threading.Condition()
mutex.acquire()
mutex.notify()
mutex.release()

