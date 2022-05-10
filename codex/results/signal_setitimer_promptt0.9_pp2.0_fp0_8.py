import signal
# Test signal.setitimer()


import os, signal
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)
# ...
pid = os.fork()
if pid == 0:
  print "Child started"
  while True: pass
  # ...
  print "Child finished"
  os._exit(0)

pid2, status = os.waitpid(pid, 0)
print "Parent knows child", pid, "exited with status", status
