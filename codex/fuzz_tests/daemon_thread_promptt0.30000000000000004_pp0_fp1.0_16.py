import threading
# Test threading daemon
def test_daemon():
    print("test_daemon start")
    time.sleep(2)
    print("test_daemon end")

def main():
    print("main start")
    t = threading.Thread(target=test_daemon)
    t.setDaemon(True)
    t.start()
    print("main end")

if __name__ == '__main__':
    main()
