import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()

# Runnable
# class PrintThread(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print(self.name)

# thread1 = PrintThread('Thread 1')
# thread2 = PrintThread('Thread 2')
# thread1.start()
# thread2.start()

# class PrintThread(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print(self.name)

# thread1 = PrintThread('Thread 1')
# thread2 = PrintThread('Thread 2')
# thread1.start()
# thread2.start()

# class PrintThread(threading.Thread):
#     def __init__(
