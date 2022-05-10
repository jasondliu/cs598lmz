import threading
# Test threading daemon, stock is a list
lock = threading.Lock()
def do_this(what):
    whoami(what)
def whoami(what):
    lock.acquire()
    print('Thread %s says: %s' % (threading.current_thread(), what))
    lock.release()
if __name__ == '__main__':
    whoami('I am the main program')
    for n in range(4):
        p = threading.Thread(target=do_this,
                             args=('I am function %s' % n,))
        p.start()
 
# 可以看到, whoami()函数，它每次被调用时，都会给主程序加一个新的线程，
# 这些线程传入的参数是自身的意识。
# 在who
