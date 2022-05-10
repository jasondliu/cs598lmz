import sys, threading

def run():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n<5:
        n = n+1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended.' % threading.current_thread().name)

def main():
    print('Thread %s is running...' % (threading.current_thread().name))
    t = threading.Thread(target=run, name='new_thread')
    t.start()
    t.join()
    print('Thread %s ended.' % threading.current_thread().name)

if __name__=='__main__':
    main()
