import threading
# Test threading daemon mode
class counter(threading.Thread):
    def __init__(self,count):
        threading.Thread.__init__(self)
        self.counter = count
    def run(self):
        threadname = threading.currentThread().getName()
        while self.counter:
            print("[%s] => %s" %(threadname,self.counter))
            time.sleep(2)
            self.counter -= 1

#list threads
threads = []
for i in range(10):
    threads.append(counter(3))

#start thread
for t in threads:
    t.setDaemon(True)
    t.start()

#wait all threads end
for t in threads:
    t.join()

print("main thread exit")
