import signal
# Test signal.setitimer() output - taking an additional argument (optional mode)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
# Test signal.setitimer() output - Python 3.2+
signal.setitimer(signal.ITIMER_REAL, 0.1)
# Test signal.setitimer() output - Python 3.3+
signal.setitimer(signal.ITIMER_MONOTONIC, 0.1)
# Test signal.pthread_sigmask() output - taking multiple signals simultaneously
signal.pthread_sigmask(signal.SIG_SETMASK, [signal.SIGUSR1, signal.SIGUSR2])
# Test signal.pthread_sigmask() output - taking multiple signals simultaneously
signal.pthread_sigmask(signal.SIG_SETMASK, [signal.SIGUSR1, signal.SIGUSR2], [signal.SIGUSR3, signal.SIGUSR4])
# Test signal.pthread_s
