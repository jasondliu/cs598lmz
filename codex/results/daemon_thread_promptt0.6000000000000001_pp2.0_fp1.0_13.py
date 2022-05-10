import threading
# Test threading daemon

# class MyThread(threading.Thread):
#     def __init__(self, target, args=(), name=None):
#         super().__init__(target=target, args=args, name=name)
#         self.daemon = True
#         self._stop = threading.Event()

#     def run(self):
#         while not self.stop():
#             self.target(*self.args)

#     def stop(self):
#         self._stop.set()

#     def stopped(self):
#         return self._stop.isSet()

# def test_func(num):
#     print(num)
#     time.sleep(0.1)

# thread = MyThread(target=test_func, args=(1,), name="test_thread")
# thread.start()

# time.sleep(0.5)
# thread.stop()
# time.sleep(0.5)
# if thread.stopped():
#     print("Thread stopped")
# else:
#     print("Thread alive")


