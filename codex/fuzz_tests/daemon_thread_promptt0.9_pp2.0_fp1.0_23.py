import threading
# Test threading daemon
# def xml_map(x):
#     y = x + 1
#     print(y)
#
#
# class myThread(threading.Thread):
#     """docstring for myThread"""
#     def __init__(self, arg):
#         super(myThread, self).__init__()
#         self.arg = arg
#
#     def run(self):
#         print('Start Downloading File ' + self.arg)
#
#
# def DownloadFile():
#     t1 = myThread('1')
#     t2 = myThread('2')
#     t3 = myThread('3')
#     print(threading.activeCount())
#     print(threading.enumerate())
#     print(threading.currentThread())
#     t1.setDaemon(True)
#     t2.setDaemon(True)
#     t1.start()
#     t2.start()
#     t3.start()
#     while (True):
#         print('-----------------')
#         time.sleep(3
