import threading
# Test threading daemon
def daemon():
    print('Start Daemon')
    time.sleep(2)
    print('Exit Daemon')

if __name__ == '__main__':
    t = threading.Thread(target=daemon)
    t.setDaemon(True)
    t.start()
    t.join()

# Test threading lock
class Mythread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print('{} start'.format(self.name))
        thread_lock.acquire()
        print_time(self.name, self.delay)
        thread_lock.release()

thread_lock = threading.Lock()
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('{}: {}'.format(thread_name, time.ctime(time.time()
