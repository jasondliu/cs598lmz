import threading
# Test threading daemon
def test_thread():
    while True:
        print("test thread")
        time.sleep(1)

def main():
    t = threading.Thread(target=test_thread)
    t.setDaemon(True)
    t.start()
    while True:
        print("main thread")
        time.sleep(1)

if __name__ == '__main__':
    main()
