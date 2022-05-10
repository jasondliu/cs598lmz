import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

if __name__ == '__main__':
    t = threading.Thread(target=test_daemon)
    t.setDaemon(True)
    t.start()
    print('main thread')
    time.sleep(1)
    print('main thread end')

# Test threading lock
# import threading
#
# class MyThread(threading.Thread):
#     def __init__(self, thread_id, name, counter):
#         threading.Thread.__init__(self)
#         self.thread_id = thread_id
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print('start thread:', self.name)
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         threadLock.release()
#
# def print_time(thread_name, delay, counter):
#    
