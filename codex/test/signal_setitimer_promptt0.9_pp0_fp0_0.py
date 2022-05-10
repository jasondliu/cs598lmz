import signal
# Test signal.setitimer to make sure it doesn't assert
signal.setitimer(signal.ITIMER_REAL, 1.0, 1.0)

# "-" as the first character of mode will make the file auto-deleted
fd = os.open(TESTFN, os.O_CREAT | os.O_RDWR)
os.write(fd, "foo")
os.close(fd)
fd = os.open(TESTFN, os.O_CREAT | os.O_RDWR | os.O_TRUNC)
