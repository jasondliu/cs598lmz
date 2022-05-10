import sys, threading

def run():
    print(threading.current_thread().getName(), 'Starting')
    for i in range(1, 10):
        print(threading.current_thread().getName(), 'Running', i)
    print(threading.current_thread().getName(), 'Exiting')

def main():
    print(threading.current_thread().getName(), 'Starting')
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print(threading.current_thread().getName(), 'Exiting')

if __name__ == '__main__':
    main()
