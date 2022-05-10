import sys, threading

def run():
    while True:
        try:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    threading.Thread(target=run).start()
    print('Press Ctrl-C to stop.')
