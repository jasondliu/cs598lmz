import threading
# Test threading daemon
# import threading
# import time
#
#
# class Mythread(threading.Thread):
#     def __init__(self, n, sleep_time):
#         super(Mythread, self).__init__()
#         self.n = n
#         self.sleep_time = sleep_time
#         self.daemon = True  # 设定守护线程
#
#     def run(self):
#         for i in range(self.n):
#             print("running{}".format(i))
#             time.sleep(self.sleep_time)
#
#
# t = Mythread(100, 0.1)
# t.start()

# using multiprocessing for training
# import multiprocessing as mp
# import time
#
#
# def job(q, a, b):
#     res = 0
#     for i in range(1000):
#         res += (a ** 2) + (b ** 3)
#     q.put(res)
#
#

