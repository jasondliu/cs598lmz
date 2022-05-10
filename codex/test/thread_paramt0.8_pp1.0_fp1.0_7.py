import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread')).start()
if __name__ == '__main__':
    print('main')
thread
main
