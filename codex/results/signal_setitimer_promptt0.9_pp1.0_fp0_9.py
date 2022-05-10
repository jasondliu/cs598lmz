import signal
# Test signal.setitimer
from signal import ITIMER_REAL, ITIMER_VIRTUAL
signal.setitimer(ITIMER_VIRTUAL, 1, 0)
signal.setitimer(ITIMER_REAL, 1, 0)


# Make sure paths are correct
# PyStone and Scimark2
import PyStoneMain
import scimark2
# unix only:
try:
    import fcntl
except ImportError:
    pass
# Mac OS X only:
try:
    import StringIO
    import macfs
    import macostools
    import macpath
    import ic
    import gestalt
    import EasyDialogs
    from Carbon import MiniAEFrame, AE as AE
except ImportError:
    pass

# Zope
import Zope.__init__
# OpenSSL and try
import M2Crypto.__init__
import cStringIO, cPickle

# PIL
# This can only succeed if the optional PIL extensions are built
try:
    from PIL import Image, GifImagePlugin, JpegImagePlugin, TiffImagePlugin
