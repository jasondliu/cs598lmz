import sys, threading

def run():
    while True:
        try:
            print(threading.current_thread().name, 'start')
            time.sleep(1)
            print(threading.current_thread().name, 'end')
        except KeyboardInterrupt:
            sys.exit()

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=run, name='thread-{}'.format(i))
        t.start()
