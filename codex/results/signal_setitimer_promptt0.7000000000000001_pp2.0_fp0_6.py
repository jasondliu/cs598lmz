import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0)  # Set timeout to 0.5 seconds
for i in range(10):
    # Timeout will be raised here
    print('Hello world')

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.2)  # Set timeout to 0.5 seconds, repeat to 0.2 seconds
for i in range(10):
    # Timeout will be raised here
    print('Hello world')

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0, 0.2)  # Set timeout to 0.2 seconds
for i in range(10):
    # Timeout will be raised here
    print('Hello world')

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0, 0)  # Disable timeout
for i in range(10):
    # Timeout will be raised here
   
