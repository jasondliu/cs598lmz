import signal
# Test signal.setitimer
paused = False

def signal_handler(sig, frame):
    global paused
