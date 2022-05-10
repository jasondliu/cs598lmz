import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, lambda s,f: print(time.time()))
time.sleep(5)
# Signal doesn't seem to be sent during sleep()

# Test exceptions
try:
    raise TypeError("foo")
except TypeError as e:
    print(e)

# Test os.fork()
def test_fork():
    # The return value (process id or -1) is returned
    pid = os.fork()
    if pid == 0:
        # In the child, return 1
        os._exit(1)
    # In the parent, return the pid
    return pid

print(test_fork())
print(test_fork())
print(test_fork())

# Test context switching
