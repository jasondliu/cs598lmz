import signal
# Test signal.setitimer
def handler(signum, frame):
  print('Signal handler called with signal ', signum)
  raise IOError('Signal handler called')

old = signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL,2)
sleep(3)
print('setitimer: Over')

# Test signal.alarm
signal.alarm(2)
sleep(3)
print('alarm: Done')

# Test os.kill
timeout = 5
pid = os.getpid()
child = subprocess.Popen(['python2.7', '-c', 'import os; import time; time.sleep(%d); os.kill(%d, %d)' % (timeout, pid, signal.SIGALRM)], stdout=subprocess.PIPE)
