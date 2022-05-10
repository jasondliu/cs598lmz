import sys, threading

def run():
    print('But in another thread: {0}'.format(sys.argv[1]))

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    import time

    print('In main thread')
    for itervar in range(10):
        time.sleep(1)
        print('count = {0}'.format(itervar))
