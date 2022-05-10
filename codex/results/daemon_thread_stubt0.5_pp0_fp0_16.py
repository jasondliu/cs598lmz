import sys, threading

def run():
    while True:
        print('Thread %s is running...' % threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    print('Thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=run, name='LoopThread')
    t.start()
    t.join()
    print('Thread %s ended.' % threading.current_thread().name)
