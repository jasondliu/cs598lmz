import threading
# Test threading daemon mode

def test_threading_daemon():
    def worker():
        print("worker")
        time.sleep(1)
        print("worker")

    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

    print("main thread")

if __name__ == "__main__":
    test_threading_daemon()
