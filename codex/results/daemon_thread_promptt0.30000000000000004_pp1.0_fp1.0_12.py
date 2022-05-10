import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('exit')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=test_daemon)
    d.setDaemon(True)
    d.start()
    d.join(1)
    print('main exit.')

# Test threading lock
# import threading
# import time
#
# class Box(object):
#     lock = threading.RLock()
#     def __init__(self):
#         self.total_items = 0
#
#     def execute(self, n):
#         Box.lock.acquire()
#         self.total_items += n
#         Box.lock.release()
#
#     def add(self):
#         Box.lock.acquire()
#         self.execute(1)
#         Box.lock.release()
#
#     def remove(self):
#         Box.lock.acquire()
#         self.execute(-1)
