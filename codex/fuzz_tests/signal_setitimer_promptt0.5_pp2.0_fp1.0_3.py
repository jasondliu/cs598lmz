import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, lambda signum, frame: None)

# Test signal.set_wakeup_fd
signal.set_wakeup_fd(1)

# Test os.kill
os.kill(os.getpid(), signal.SIGALRM)

# Test os.killpg
os.killpg(os.getpgid(os.getpid()), signal.SIGALRM)

# Test os.kill
os.kill(os.getpid(), signal.SIGALRM)

# Test os.killpg
os.killpg(os.getpgid(os.getpid()), signal.SIGALRM)

# Test os.kill
os.kill(os.getpid(), signal.SIGALRM)

# Test os.killpg
os.killpg(os.getpgid(os.getpid()), signal.SIGALRM)

# Test os.kill
os.kill
