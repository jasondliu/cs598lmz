import threading
# Test threading daemon thread

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.daemon = True
        self.start()

    def run(self):
        print('Starting thread: ' + self.name)
        time.sleep(3)
        print('Exiting thread: ' + self.name)

def main():
    print('Start main thread')
    MyThread('Daemon thread')
    time.sleep(1)
    print('Exit main thread')

if __name__ == '__main__':
    main()
