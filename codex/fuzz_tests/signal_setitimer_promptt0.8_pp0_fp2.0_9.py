import signal
# Test signal.setitimer()

def handler(*args):
    print('args =', args)
    if len(args) == 3:
        print('itimer expires')
        signal.setitimer(signal.ITIMER_REAL, 0)
        print('itimer stopped')

print('Setting handler ...')
signal.signal(signal.SIGALRM, handler)

print('Setting itimer ...')
signal.setitimer(signal.ITIMER_REAL, 2)

print('Waiting 3 secs ...')
time.sleep(3)
# args = (14, 0)
# itimer expires
# itimer stopped

print('Done')
