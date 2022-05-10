import threading
# Test threading daemon
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(threading.current_thread().name)

def test_threading():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    test_threading()
