import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_REAL, 0, 0)

# Test select.select()
select.select([], [], [], 1)
select.select([], [], [], 0)

# Test time.sleep()
time.sleep(1)
time.sleep(0)

# Test os.system()
os.system('sleep 1')
os.system('true')

# Test os.fork() and os.wait()
pid = os.fork()
if pid:
    os.waitpid(pid, 0)
else:
    sys.exit(0)

# Test os.popen()
p = os.popen('sleep 1')
p.close()

# Test os.exec*()
pid = os.fork()
if pid == 0:
    os.execvp('sleep', ['sleep', '1'])
    sys.exit(1)
os.waitpid(pid, 0)

# Test os.spawn
