import sys, threading

def run():
    while True:
        sys.stdout.write('(%s) hello world\n' % threading.current_thread().name)
        sys.stdout.flush()

if __name__ == '__main__':
    t = threading.Thread(name='background', target=run)
    t.daemon = True
    t.start()
    print('[%s] started' % threading.current_thread().name)
    t.join()
    print('[%s] joined' % threading.current_thread().name)
