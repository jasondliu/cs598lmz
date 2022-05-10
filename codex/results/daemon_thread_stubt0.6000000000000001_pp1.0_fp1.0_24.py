import sys, threading

def run():
    flag = 0
    while flag < 10:
        print('thread %s is running' % threading.current_thread().name)
        flag += 1
        time.sleep(1)

if __name__ == '__main__':
    print('thread %s is running' % threading.current_thread().name)
    t = threading.Thread(target=run, name='T')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
