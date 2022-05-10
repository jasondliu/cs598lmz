import sys, threading

def run():
    while True:
        s = raw_input('enter command: ')
        print 'processing...'
        time.sleep(3)
        print 'processed: {}'.format(s)


thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit(1)
