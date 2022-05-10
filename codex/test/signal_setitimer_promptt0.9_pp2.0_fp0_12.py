import signal
# Test signal.setitimer(2) for SIG_BLOCK
try:
    signal.setitimer(2, 1)
except:
    print('Test succeeded.')
else:
    print('Test failed.')
# Test signal.siginterrupt(17, 1)
try:
    signal.siginterrupt(17, 1)
except:
    print('Test succeeded.')
else:
    print('Test failed.')
# Test signal.signal(17, 1)
try:
    signal.signal(17, 1)
except:
    print('Test succeeded.')
else:
    print('Test failed.')
# Test signal.sigpending()
try:
    signal.sigpending()
except:
    print('Test succeeded.')
else:
    print('Test failed.')
# Test signal.sigwait([1, 2])
try:
    signal.sigwait([1, 2])
except:
    print('Test succeeded.')
else:
    print('Test failed.')
# Test signal.sigwaitinfo([1, 2])
