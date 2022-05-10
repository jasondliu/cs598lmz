import threading
# Test threading daemon
if __name__ == "__main__":
    def func():
        print 'hello timer'
        global timer
        timer = threading.Timer(2, func)
        timer.start()

    func()
    time.sleep(10)
    timer.cancel()
