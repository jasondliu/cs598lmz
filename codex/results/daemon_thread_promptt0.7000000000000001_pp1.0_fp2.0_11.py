import threading
# Test threading daemon thread
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print("Thread:", self.name, i)

if __name__ == "__main__":
    t = MyThread()
    t.daemon = True
    t.start()

    # Main thread waits for t thread to finish
    t.join()
    print("t.is_alive:", t.is_alive())
