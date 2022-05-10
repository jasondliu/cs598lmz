import signal
# Test signal.setitimer on FreeBSD.
#
# setitimer() is a very old BSD syscall, which has been fine for about ten years.
#
# The syscall interface is hideous and mind-bendingly difficult to use.
# I recommend glancing at the OpenBSD source code for inspiration.
# Fortunately, Python has excellent Signal support.
# Python's timers are vastly better than system timers.
#
# On FreeBSD 10+, the timer actually works well.
# On FreeBSD 8.x and 9.x, pthread_sigmask() is broken by design.
#
# pywatch/pw-client.py uses this code on the client.
# pywatch/pw-server.py uses this code on the server.
#

try:
	import fcntl
except ImportError:
	pass
else:
	TIOCGWINSZ = getattr(fcntl, "TIOCGWINSZ", 1074295912)
	TIOCSWINSZ = getattr(fcntl, "TIOCSWINSZ", -2146929561)
	def get_winsz(fd=0):
