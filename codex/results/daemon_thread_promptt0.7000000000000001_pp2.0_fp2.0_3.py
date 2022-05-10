import threading
# Test threading daemon 
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
    def run(self):
        global stop_all
        while True:
            if stop_all:
                break
            print("I am " + self.name)
            time.sleep(1)

stop_all = False
t1 = MyThread("Thread-1")
t2 = MyThread("Thread-2")

t1.start()
t2.start()
time.sleep(3)
stop_all = True

# Test threading join()
def job(name):
    print("Hello I am %s" % name)

t = threading.Thread(target=job, name="Tedu", args=("Tedu.cn",))
t.start()
t.join()
print("I am main thread")

# Test threading lock
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1
        print
