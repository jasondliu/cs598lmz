import sys, threading

def run():
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    thread = threading.Thread(target=run, name='my_thread')
    thread.start()
    thread.join()
    print(threading.current_thread().name)
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread().is_alive())
    print(threading.current_thread().ident)
    print(threading.current_thread().name)
    print(threading.current_thread().daemon)
    print(threading.current_thread().isDaemon())
    print(threading.current_thread().is_alive())
