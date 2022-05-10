import signal
# Test signal.setitimer, signal.setitimer_ns, signal.getitimer and
# signal.getitimer_ns.
if hasattr(signal, 'setitimer'):
    with captured_output('stderr') as c:
        signal.setitimer(signal.ITIMER_PROF, 1.0, 2.0)
    print(c.getvalue())
    with captured_output('stderr') as c:
        signal.getitimer(signal.ITIMER_PROF)
    print(c.getvalue())
if hasattr(signal, 'setitimer_ns'):
    with captured_output('stderr') as c:
        signal.setitimer_ns(signal.ITIMER_PROF, 1000000000, 2000000000)
    print(c.getvalue())
    with captured_output('stderr') as c:
        signal.getitimer_ns(signal.ITIMER_PROF)
    print(c.getvalue())
# Test signal.set_wakeup_fd, signal.set_wakeup_
