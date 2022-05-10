import threading
threading.current_thread().name
#'MainThread'
#为线程指定名称
import threading
class MyThread(threading.Thread):
    def run(self):
        print(self.name+' is running...')
t1=MyThread()
t1.start()
#Thread-1 is running...
#关于线程优先级
#线程的优先级高并不表示它会先执行完，而是指执行机会会多一些
#线程的优先级分为0-19这20级，分别用整数来表示，数值越大优先级越高，默认优先
