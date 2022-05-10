import signal
if hasattr(signal, 'setitimer'):
    def handler(*args):
        raise KeyboardInterrupt
    signal.setitimer(signal.ITIMER_REAL, 0.001)
    try:
        exec("1 + 1")
    except SystemExit:
        pass
