import threading
threading.stack_size(67108864)

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print(threading.current_thread().getName())

for i in range(100):
    my_thread = MyThread()
    my_thread.start()
