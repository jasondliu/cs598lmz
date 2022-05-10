import threading
# Test threading daemon
# import time
# import random
# import threading
#
# def worker():
#     """thread worker function"""
#     t = threading.currentThread()
#     pause = random.randint(1,5)
#     print 'sleeping %s' % pause
#     time.sleep(pause)
#     print 'ending'
#     return
#
# threads = []
# for i in range(3):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()
#
# print threads

# class MyThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print "Starting " + self.name
#         print_time(self.name, self.counter, 5)
#         print "Exiting " + self.name
