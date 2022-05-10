import threading
threading.stack_size(1024*1024*1000)

class MyThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        print("Thread {0} is running".format(self.id))
        print("{0} is done".format(self.id))



if __name__ == '__main__':
    for i in range(5):
        t = MyThread(i)
        t.start()
