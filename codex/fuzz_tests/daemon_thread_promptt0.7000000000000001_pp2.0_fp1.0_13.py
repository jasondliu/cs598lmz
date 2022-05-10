import threading
# Test threading daemon threads
#
# t = threading.Thread(target=testThreading, args=(5, "John Smith"))
# t.setDaemon(True)
# t.start()
# t.join()


# #############################################################################
# Listing all the threads currently running
#
# import time
# import threading
#
# def testThreading(name, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print(name + ": " + str(time.ctime(time.time())))
#
# # Testing threading
# t1 = threading.Thread(target=testThreading, args=("Thread-1", 2))
# t2 = threading.Thread(target=testThreading, args=("Thread-2", 4))
# t1.start()
# t2.start()
#
# print("Active Threads: " + str(threading.active_count()))
# print("Thread Objects: " + str(threading.enumerate()))



