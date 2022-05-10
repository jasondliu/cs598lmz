import threading
# Test threading daemon
# def daemon():
#     print('Start')
#     time.sleep(5)
#     print('End')
#
# if __name__ == '__main__':
#     d = threading.Thread(target=daemon)
#     d.setDaemon(True)
#     d.start()
#     d.join(2.5)
#     print('Main thread end')

# Test threading lock
# class Counter(object):
#     def __init__(self):
#         self.lock = threading.Lock()
#         self.value = 0
#
#     def increment(self):
#         self.lock.acquire()
#         self.value = value = self.value + 1
#         self.lock.release()
#         return value
#
# counter = Counter()
# lock = threading.Lock()
#
# def worker(sensor_index):
#     while True:
#         lock.acquire()
#         print('Sensor %d' % counter.increment())
#         lock.release()
#         time
