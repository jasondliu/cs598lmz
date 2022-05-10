import signal
# Test signal.setitimer() on Solaris
setitimer.SIG = signal.SIGVTALRM
setitimer.VALUE = 20

istest.run()
