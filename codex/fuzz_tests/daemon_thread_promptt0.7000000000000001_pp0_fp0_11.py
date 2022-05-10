import threading
# Test threading daemon
# import threading

# class TestThread(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name	

#     def run(self):
#         print("Thread %s is running!" %self.name)
#         for i in range(1, 10):
#             print("%s is running %d times!" %(self.name, i))
#             time.sleep(1)

# if __name__ == '__main__':
#     thread1 = TestThread("Thread1")
#     # thread1.setDaemon(True)
#     thread2 = TestThread("Thread2")
#     thread1.start()
#     thread2.start()
#     thread1.join(3)
#     print("thread1 is over")
    

# Test threading lock
# import threading
# import time
# import random

# class TestThread(threading.Thread):
#     def __init__(self, name, lock, sleep = 2
