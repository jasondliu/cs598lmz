import select
# Test select.select() with a signal handler.
import signal
import sys
import time
import os

if not hasattr(select, "poll"):
    print("poll() not supported")
    sys.exit(0)

# Check that the signal handler is called
signal_received = False
oldalrm = signal.signal(signal.SIGALRM, lambda sig, frame: signal_received)

def set_alarm():
    signal_received = False
    signal.alarm(1)

def alarm_handler(sig, frame):
    global signal_received
    signal_received = True
    signal.alarm(0)

signal.signal(signal.SIGALRM, alarm_handler)

# Check select()
set_alarm()
signal.pause()
if not signal_received:
    raise RuntimeError("SIGALRM not received")

# Check poll()
set_alarm()
poll = select.poll()
poll.poll(1000)
if not signal_received:
    raise RuntimeError("SIGALRM not received")
