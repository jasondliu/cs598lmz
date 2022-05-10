import sys, threading

def run():
    while True:
        print('Thread is running')
        time.sleep(1)

def test():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    t.join()
    print('thread end')

if __name__ == '__main__':
    test()
    print('main thread end')
