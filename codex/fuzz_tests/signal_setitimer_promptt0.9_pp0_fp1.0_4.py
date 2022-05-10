import signal
# Test signal.setitimer
#
# This test program is expected to output 'SUCCESS' and exit(0).
#
def cleanup():
    sys.exit(0)

# Define signal handlers
def alarm_handler( sig, frame ):
    print('SUCCESS')
    cleanup()

# Install signal handlers
signal.signal(signal.SIGALRM, alarm_handler)

# Set ITIMER_REAL timer for 5 seconds.
signal.setitimer(signal.ITIMER_REAL, 5, 0)

# Wait for signal
try:
    signal.pause()
except KeyboardInterrupt:
    # Process interrupted by user
    cleanup()
