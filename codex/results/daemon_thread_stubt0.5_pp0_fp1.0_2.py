import sys, threading

def run():
    print('Thread name:', threading.current_thread().name)
    print('Thread is running...')

def main():
    t = threading.Thread(target=run, name='my_thread')
    t.setDaemon(True)
    t.start()
    t.join()
    print('Thread name:', threading.current_thread().name)
    print('Thread ended.')

if __name__ == '__main__':
    main()
