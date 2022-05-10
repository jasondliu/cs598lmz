import threading
# Test threading daemon
def f():
    print('thread function')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        print(t.getName())
        t.join()

# Test threading lock
import threading

def f():
    global x
    for i in range(100):
        x += 1
        print(x)

if __name__ == '__main__':
    x = 0
    lock = threading.Lock()
    for i in range(2):
        t = threading.Thread(target=f)
        t.start()
