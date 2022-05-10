import threading
# Test threading daemon
# def timer(no, interval):
#     cnt = 0
#     while cnt < 10:
#         print('Thread:(%d) Time:%s\n' % (no, time.ctime()))
#         time.sleep(interval)
#         cnt += 1
#     threading.currentThread

# threading.current_thread().setName('MainThread')
# thread1 = threading.Thread(target=timer, args=(1, 1))
# thread2 = threading.Thread(target=timer, args=(2, 2))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print('Thread:(%s) Time:%s\n' % (threading.current_thread().name, time.ctime()))

# Test threading lock
# class Account:
#     def __init__(self, _id, balance, lock):
#         self.id = _id
#         self.balance = balance
#         self.lock = lock
    
#    
