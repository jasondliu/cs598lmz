import signal
# Test signal.setitimer() and signal.getitimer()

def handler(signum, frame):
    "Handler for SIGALRM."
