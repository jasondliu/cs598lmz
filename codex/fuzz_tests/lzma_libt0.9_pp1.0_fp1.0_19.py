import lzma
lzma = __import__('lzma')
__all__.append('lzma')

from . import _probablybuffer
_probablybuffer = __import__('_probablybuffer')
__all__.append('_probablybuffer')

from . import _compat_pickle
_compat_pickle = __import__('_compat_pickle')
__all__.append('_compat_pickle')

from . import cPickle
cPickle = __import__('cPickle')
__all__.append('cPickle')


if sys.platform == 'win32':
    def _copyfileobj_readinto(fsrc, fdst, length=1024*1024):
        """shutil.copyfileobj()[1], but uses readinto()."""
        while True:
            buf = fsrc.read(length)
            if not buf:
                break
            fdst.write(buf)
elif ((sys.version_info[:3] >= (3, 2, 5)) or
      (sys.version_info[:3] >= (
