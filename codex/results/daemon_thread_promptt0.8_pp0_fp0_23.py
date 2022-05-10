import threading
# Test threading daemon
import multiprocessing
import time
import traceback

def test_thread(name, event):
    if event.is_set():
        print('event has been set')
    event.set()
    if event.is_set():
        print('event has been set')
        print('event wait')
        event.wait(10)
        print('event wait end')


if __name__ == '__main__':
    event = threading.Event()
    th1 = threading.Thread(target=test_thread, args=('test_thread1',event))
    th2 = threading.Thread(target=test_thread, args=('test_thread2',event))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('thread end')
