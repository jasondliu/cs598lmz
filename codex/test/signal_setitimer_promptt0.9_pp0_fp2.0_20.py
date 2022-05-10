import signal
# Test signal.setitimer.
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
print('FOO')

sys.stdout.flush()
time.sleep(1)

print('BAR')

if sys.platform.startswith('win'):
    # On Windows, raise a keyboard interrupt.
    import msvcrt

    msvcrt.getch()
else:
    # On other platforms, use a POSIX signal.
    os.kill(os.getpid(), signal.SIGUSR1)
"""


def main(args):
    """
