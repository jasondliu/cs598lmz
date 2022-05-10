import signal
# Test signal.setitimer(), works on Linux, OS X or Cygwin, not Windows.
if os.name == 'posix':
    signal.setitimer(signal.ITIMER_REAL, 0.2)
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.2)
    signal.setitimer(signal.ITIMER_PROF, 0.2)

from . import sunau
from . import sndhdr
from . import lsfmod
from . import audiodata
from . import aifc
from . import wave
from . import chirp
from . import colorsys
from . import imghdr
from . import sndhdr
from . import ossaudiodev

from .__main__ import detect_encoding, open
from .__main__ import StringIO, BytesIO
from .__main__ import int2byte, _intstruct
