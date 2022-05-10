import signal
# Test signal.setitimer with an unset signo
rc = True
def handler(signum, frame):
    global rc
    rc = False

# Get status of all signals
def save_signal_mask():
    mas
