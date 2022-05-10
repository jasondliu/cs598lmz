import sys, threading

def run():
    print('Thread {} is running'.format(threading.current_thread().name))

if __name__ == '__main__':
    print('Thread {} is running'.format(threading.current_thread().name))
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('Thread {} is ended'.format(threading.current_thread().name))
