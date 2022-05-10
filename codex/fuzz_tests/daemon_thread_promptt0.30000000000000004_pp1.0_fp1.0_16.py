import threading
# Test threading daemon
import time

def test_thread(name):
    while True:
        print(name)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test_thread, args=('t1',), daemon=True)
    t2 = threading.Thread(target=test_thread, args=('t2',), daemon=True)
    t1.start()
    t2.start()
    time.sleep(5)
    print('main thread exit')

if __name__ == '__main__':
    main()
