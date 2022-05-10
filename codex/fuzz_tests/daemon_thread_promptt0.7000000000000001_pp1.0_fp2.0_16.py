import threading
# Test threading daemon

# class A(threading.Thread):
#     def __init__(self):
#         super(A, self).__init__()
#         self.daemon = True

#     def run(self):
#         while True:
#             print('A')
#             time.sleep(2)

# class B(threading.Thread):
#     def __init__(self):
#         super(B, self).__init__()
#         self.daemon = True

#     def run(self):
#         while True:
#             print('B')
#             time.sleep(3)

# a = A()
# b = B()
# a.start()
# b.start()
# time.sleep(10)

# from multiprocessing import Process
# import matplotlib.pylab as plt
# import numpy as np
# import time

# class proc(Process):
#     def __init__(self):
#         super(proc, self).__init__()
#         self.daemon = True

