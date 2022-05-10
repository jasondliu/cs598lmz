import threading
threading.stack_size(67108864)

def func():
    print('thread function')
    time.sleep(1)
    print('thread function end')

if __name__ == '__main__':
    t = threading.Thread(target=func)
    t.start()
    t.join()
    print('main thread end')
