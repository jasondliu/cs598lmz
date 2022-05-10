import sys, threading

def run():
    while True:
        time.sleep(1)
        print('thread %s is running...' % threading.current_thread().name)

def main():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=run, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

if __name__ == '__main__':
    main()
