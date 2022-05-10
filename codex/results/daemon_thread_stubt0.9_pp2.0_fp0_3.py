import sys, threading

def run():
    sys.stdout.write('I am child\n')
    sys._stdout.flush()

if __name__ == '__main__':
    thread = threading.Thread(name='child', target=run)
    
    try:
        thread.start()
    except (KeyboardInterrupt, SystemExit):  # noqa
        sys.exit('Quitting')

# vim: et sw=4 sts=4
