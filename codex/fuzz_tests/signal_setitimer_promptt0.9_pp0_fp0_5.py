import signal
# Test signal.setitimer by playing with SIGALRM


def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 5, 0)

# This open() may hang indefinitely
fd = os.open('/dev/tty', os.O_RDWR)

os.write(fd, 'About to do sys.exit()\n')

sys.exit()



class TestImports:

  def test_1(self):
    import exceptions
    import string
    import types
    import UserList
    
  def test_2(self):
    import UserString
    import UserDict
    import _LWPCookieJar
    import _MozillaCookieJar
    import audiodev
    import ConfigParser
    import Cookie
    import cookielib
    import Image
    import imghdr
    import mimetools
    import mmsystem
    
 
