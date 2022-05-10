import sys, threading

def run():

    while True:
        cmd = raw_input('> ')
        if cmd == 'quit':
            sys.exit()
        print 'start'
        time.sleep(3)
        print 'end'

thread = threading.Thread(target=run)
thread.start()
