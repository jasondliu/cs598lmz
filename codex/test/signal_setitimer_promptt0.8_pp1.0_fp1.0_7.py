import signal
# Test signal.setitimer
print('Checking signal.setitimer: ', end=' ')
signal.signal(signal.SIGALRM, lambda *args: None)
signal.setitimer(signal.ITIMER_REAL, 0.2)
time.sleep(1.0)
signal.setitimer(signal.ITIMER_REAL, 0.0)
print('ok')

# Test thread
print('Checking thread module: ', end=' ')
import thread
thread.get_ident()
print('ok')

# Test sys.args
print('Checking sys.argv: ', end=' ')
print(sys.argv)
print('ok')

# Test sys.exit
print('Checking sys.exit(): ', end=' ')
try:
    sys.exit(0)
except SystemExit:
    print('ok')

# Test sys.float_info
print('Checking sys.float_info: ', end=' ')
print(sys.float_info)
print('ok')

# Test sys.maxsize
