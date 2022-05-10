import signal
# Test signal.setitimer() and signal.getitimer()

# The default behavior is to throw a KeyboardInterrupt exception
# after 5 seconds.  This can be changed using the -t option.
timer = 5

def handler(signum, frame):
    print "I'm sorry, I cannot do that."

def set_timer(new_value):
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, new_value)

def main():
    global timer
    # install the signal handler and set the timer
    set_timer(timer)
    try:
        while 1:
            pass
    except KeyboardInterrupt:
        print '\nokay, okay, I will stop now'
        timer = signal.getitimer(signal.ITIMER_REAL)
        print 'the timer was set to %.1f' % timer[0]

if __name__ == '__main__':
    main()
