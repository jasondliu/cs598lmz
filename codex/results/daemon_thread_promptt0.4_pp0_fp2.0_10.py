import threading
# Test threading daemon
# https://stackoverflow.com/questions/19071512/python-threading-daemon-vs-none

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

def do_something2():
    print('Sleeping 2 second...')
    time.sleep(2)
    print('Done Sleeping...')

def do_something3():
    print('Sleeping 3 second...')
    time.sleep(3)
    print('Done Sleeping...')


if __name__ == '__main__':
    # t1 = threading.Thread(target=do_something)
    # t1.start()
    # t2 = threading.Thread(target=do_something2)
    # t2.start()
    # t3 = threading.Thread(target=do_something3)
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()

    # t1 = threading.Thread
