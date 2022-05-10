import signal
# Test signal.setitimer / signal.getitimer
sys.stdout.flush()
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.1)
time.sleep(1.5)
sys.stdout.write('x')
sys.stdout.flush()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(2.0)
sys.stdout.write('y')
sys.stdout.flush()
signal.setitimer(signal.ITIMER_REAL, 0, 0)
time.sleep(2.0)
sys.stdout.write('z')
sys.stdout.flush()
sys.stdout.write('\n')
# Test signal.setitimer returning the old value
sys.stdout.flush()
signal.setitimer(signal.ITIMER_REAL, 1.0, 0.1)
time.sleep(1.5)
sys.stdout.write('a')
sys.stdout.flush()
signal
