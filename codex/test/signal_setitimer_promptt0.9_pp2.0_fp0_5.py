import signal
# Test signal.setitimer
signal.setitimer(signal.ITIMER_REAL, 0.5)

# Test signal.signal
# signal.signal(signal.SIGALRM, lambda signum, frame: None)

# Test threading module
import threading
import thread
# signal.setitimer(signal.ITIMER_PROF, 0.1)
t = threading.Thread(target=lambda: signal.setitimer(signal.ITIMER_PROF, 0.1))
t.start()
# signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
t = threading.Thread(target=lambda: signal.setitimer(signal.ITIMER_VIRTUAL, 0.1))
t.start()

# Test ssl
import socket
# socket.ssl(socket.socket(), None, None)

# os.popen('ls /')

# Test _ast
import _ast
f = _ast.parse("1 + 2")
c = compile(f, '', 'exec')
