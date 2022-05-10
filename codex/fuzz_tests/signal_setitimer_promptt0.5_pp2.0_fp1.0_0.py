import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.signal(signal.SIGVTALRM, lambda x,y: print("OK"))

# Test signal.siginterrupt
signal.siginterrupt(signal.SIGINT, True)

# Test signal.getsignal
assert signal.getsignal(signal.SIGINT) == signal.default_int_handler

# Test signal.set_wakeup_fd
import _multiprocessing
signal.set_wakeup_fd(_multiprocessing.sentinel)

# Test signal.pause
signal.pause()

# Test signal.pthread_kill
signal.pthread_kill(signal.get_ident(), signal.SIGINT)

# Test signal.sigwait
signal.sigwait([signal.SIGINT])

# Test signal.sigwaitinfo
signal.sigwaitinfo([signal.SIGINT])

# Test signal.sigtim
