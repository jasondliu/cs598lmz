import threading
# Test threading daemon = True, if set True, it will quit once the main thread is done.
# Otherwise, it will continue until all the threads are done.
def worker():
    print('Thread is working.')
    return

for i in range(5):
    t = threading.Thread(target=worker)
    # t.setDaemon(True)
    t.start()

# import time
# import threading
# print('PID:%s'%(os.getpid()))
# def worker(num):
#     time.sleep(3)
#     print('Thread %s is working.'%(num))
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker,args=(i,))
#     t.start()
#     threads.append(t)
# for t in threads:
#     t.join()

# import time
# import threading
#
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread
