import threading
# Test threading daemon

def test():
    while True:
        print("test")
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=test)
    t.setDaemon(True)
    t.start()
    print("main thread")
    time.sleep(3)
    print("main thread end")
