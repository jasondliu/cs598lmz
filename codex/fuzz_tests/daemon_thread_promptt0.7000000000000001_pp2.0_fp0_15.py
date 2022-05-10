import threading
# Test threading daemon vs non-daemon
class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print('Threading ',self.num)
        time.sleep(5)

def main():
    for i in range(5):
        t=MyThread(i)
        t.setDaemon(True)
        t.start()
    print('Main thread')

if __name__=='__main__':
    main()


# Test threading lock
# lock = threading.Lock()
#
# def run(n):
#     lock.acquire()
#     global num
#     num += 1
#     lock.release()
#
# lock = threading.Lock()
# num = 0
#
# t_objs = []
#
# for i in range(50):
#     t = threading.Thread(target=run, args=('t-%s' % i,))
#     t.start()

