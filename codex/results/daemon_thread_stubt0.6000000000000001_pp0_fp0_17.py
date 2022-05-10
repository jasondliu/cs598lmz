import sys, threading

def run():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(), 'Exiting')

def main():
    print(threading.current_thread().getName(), 'Starting')
    t = threading.Thread(target=run, name='MyThread')
    t.start()
    print(threading.current_thread().getName(), 'Exiting')

if __name__ == '__main__':
    main()
</code>

