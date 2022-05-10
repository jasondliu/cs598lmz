import signal
# Test signal.setitimer
system("echo 'import signal; signal.signal(signal.SIGALRM, lambda x,y: exit()); signal.setitimer(signal.ITIMER_REAL, 0.1)' | " + sys.executable + " -u -")
# Test signal.setitimer and OSError
system("echo 'import signal; signal.signal(signal.SIGALRM, lambda x,y: exit()); signal.setitimer(signal.ITIMER_REAL, 0.1); exit(1)' | " + sys.executable + " -u -")
# Test signal.setitimer and OSError
system("echo 'import signal; signal.signal(signal.SIGALRM, lambda x,y: exit()); signal.setitimer(signal.ITIMER_REAL, 0.1); import time; time.sleep(1); exit(1)' | " + sys.executable + " -u -")

# Test signal.setitimer
