import threading
# Test threading daemon

class MyThread(threading.Thread):
    def run(self):
        print(self.getName())
        print('daemon:', self.daemon)

t = MyThread()
t.daemon = True
t.start()

print('main thread')

# Test threading lock

class MyThread(threading.Thread):
    def run(self):
        if mutex.acquire():
            print(self.name)
            mutex.release()

mutex = threading.Lock()
for i in range(5):
    t = MyThread()
    t.start()

# Test threading condition

class Producer(threading.Thread):
    def run(self):
        global L
        if con.acquire():
            for i in range(5):
                L.append(i)
                print('Produced:', i)
            con.notify()
            con.release()

class Consumer(threading.Thread):
    def run(self):
        global L
        if con.acquire():
            con.wait
