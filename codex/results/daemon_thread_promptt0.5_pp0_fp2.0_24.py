import threading
# Test threading daemon
def worker():
    print('worker')
    return
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

# Test threading lock
# import threading, time
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("Starting " + self.name)
#         # Get lock to synchronize threads
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # Free lock to release next thread
#         threadLock.release()
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.
