import signal
# Test signal.setitimer
if hasattr(signal, 'setitimer'):
    print('setitimer:', [signal.setitimer(*args)
                         for args in ((signal.ITIMER_REAL, 0, 0),
                                      (signal.ITIMER_REAL, 2, 0.2))])
    # Test signal.signal
    if hasattr(signal, 'signal'):
        print('signal:', [signal.signal(signal.SIGALRM, lambda *args: None)
                          for i in range(2)])
else:
    print('setitimer:', [None for i in range(2)])
    print('sig
