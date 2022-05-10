import signal
# Test signal.setitimer
print >>sys.stderr, "signal.setitimer:",
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
time.sleep(0.2)
print >>sys.stderr, "OK"

print >>sys.stderr
print >>sys.stderr, "execv:",
d = subprocess.Popen(('-c', 'import sys;print >>sys.stderr, "OK"'),
    executable='/bin/sh', close_fds=True)
d.wait()

print >>sys.stderr, "fork:",
d = subprocess.Popen(('-c', 'import sys;sys.exit(42)'),
    executable='/bin/sh', close_fds=True)
print >>sys.stderr, "OK", d.returncode

print >>sys.stderr
print >>sys.stderr, "pipe:",
d = subprocess.Popen(('-c', 'import sys;print "OK";sys.exit(42
