import threading
# Test threading daemon
# import time
# import threading
#
# def test_daemon():
#     while True:
#         print('hello')
#         time.sleep(1)
#
#
# t = threading.Thread(target=test_daemon)
# t.setDaemon(True)
# t.start()
# t.join()
# print('main thread')

# Test threading lock
# import logging
# import threading
# import time
#
# class FakeDatabase:
#     def __init__(self):
#         self.value = 0
#         self._lock = threading.Lock()
#
#     def update(self, name):
#         logging.info("Thread %s: starting update", name)
#         local_copy = self.value
#         local_copy += 1
#         time.sleep(0.1)
#         self.value = local_copy
#         logging.info("Thread %s: finishing update", name)
#
#
#
# if __name__ == "__main__":
#     format = "%(
