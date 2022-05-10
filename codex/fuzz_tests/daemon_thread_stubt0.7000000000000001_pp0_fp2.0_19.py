import sys, threading

def run():
    # Wait for the process to be unblocked
    print '  waiting for unblock'
    sys.stdout.flush()
    sys.stdin.read()

    # Wait for the process to have been killed
    print '  waiting for kill'
    sys.stdout.flush()
    time.sleep(20)
    print '  exiting'

t = threading.Thread(targ
