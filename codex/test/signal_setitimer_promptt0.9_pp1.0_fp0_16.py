import signal
# Test signal.setitimer
def handler ():
    raise ExitException
signal.signal(signal.SIGCHLD, handler)
signal.setitimer(signal.ITIMER_REAL, 0)
# Doesn't work properly on:
#  HP-UX 10
#  SGI IRIX 6.5
#  Solaris 8 (or earlier)
# It doesn't work with SIGCHLD, at least not on Solaris
# It doesn't work with SIGALRM on Solaris
signal.setitimer(signal.ITIMER_REAL, 4, 1)
#print os.EX_OK
time.sleep (1)
