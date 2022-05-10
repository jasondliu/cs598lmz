import signal
# Test signal.setitimer
if hasattr(signal, 'setitimer'):
    def setitimer_alarm_handler(signum, frame):
        print(signum)
        raise SystemExit(str(signum))
    print('*' * 20, 'Testing signal.setitimer starting')
    old_action = signal.signal(signal.ITIMER_REAL, setitimer_alarm_handler)
    old_itimer = signal.setitimer(signal.ITIMER_REAL, 0.01, 0)
    # Do nothing, wait for the alarm handler to be called
    print('*' * 20, 'Testing signal.setitimer ok')
try:
    # Test ctypes.cdll.LoadLibrary
    print('*' * 20, 'Preliminary tests starting')
    import ctypes
    libm = ctypes.cdll.LoadLibrary('libm.so.6')
    assert libm.sqrt(4.0) == 2.0
    print('*' * 20, 'Preliminary tests passed')
except Exception:
    print('
