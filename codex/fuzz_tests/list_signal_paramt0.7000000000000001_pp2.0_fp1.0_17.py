import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        # Re-install default SIGALRM handler
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

# Install handler for SIGALRM
signal.signal(signal.SIGALRM, handler)

# Set first timer
handler()

print("Starting loop")
while True:
    signal.pause()
