import sys, threading

def run():
    logging.debug('Thread started')
    return

def main():
    logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()

if __name__ == '__main__':
    main()
