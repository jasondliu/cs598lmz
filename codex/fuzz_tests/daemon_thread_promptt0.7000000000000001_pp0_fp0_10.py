import threading
# Test threading daemon
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(i)
            threading.Event().wait(1)

if __name__ == '__main__':
    mt = MyThread()
    mt.daemon = True
    mt.start()
    # mt.join()
    print("Bye")
