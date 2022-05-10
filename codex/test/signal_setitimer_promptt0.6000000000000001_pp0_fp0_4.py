import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_PROF, 1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
# Test signal.getitimer()
signal.getitimer(signal.ITIMER_REAL)
signal.getitimer(signal.ITIMER_PROF)
signal.getitimer(signal.ITIMER_VIRTUAL)


# Test signal.set_wakeup_fd()
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    print('Signal handler called with frame', frame)
    print('Signal handler called with frame.f_code', frame.f_code)
    print('Signal handler called with frame.f_code.co_filename',
          frame.f_code.co_filename)
