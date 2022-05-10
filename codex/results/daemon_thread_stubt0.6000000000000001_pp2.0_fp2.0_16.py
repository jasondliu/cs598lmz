import sys, threading

def run():
    print('Thread: {}'.format(threading.current_thread().name))
    sys.stdout.flush()


if __name__ == '__main__':
    print('Main: {}'.format(threading.current_thread().name))
    sys.stdout.flush()

    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
