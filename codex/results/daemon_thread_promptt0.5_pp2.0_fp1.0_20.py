import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("running on number:%s" % self.num)
        time.sleep(1)

if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start()
    t2.start()

    print(t1.getName())
    print(t2.getName())

    print(t1.is_alive())
    print(t2.is_alive())

    t1.join()
    t2.join()

    print(t1.is_alive())
    print(t2.is_alive())

    print("test end")
