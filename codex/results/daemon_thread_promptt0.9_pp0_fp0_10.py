import threading
# Test threading daemon

class MyThread(threading.Thread):
    def run(self):
        for x in range(10):
            print("I am a thread, my name is " + self.getName())
            time.sleep(5)
if __name__=='__main__':
    for t in range(2, 7):
        mythread = MyThread()
        # daemon=True: if main thread quits, child thread is also quitted 
        # if daemon=False, child thread will continue to run
        mythread.daemon = True
        mythread.start()
        time.sleep(1)
# Test threading lock
import threading
# Test threading 

class MyThreading(threading.Thread):
    def run(self):
        global count, mutex
        temp = count
        time.sleep(1)
        count = temp + 1
        mutex.acquire()
        print("I am %s, set count %s" % (self.getName(), count))
        mutex.release()
if __name__=='__main__':
    threads
