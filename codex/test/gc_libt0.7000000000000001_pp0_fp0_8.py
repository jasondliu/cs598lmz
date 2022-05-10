import gc, weakref
from itertools import chain
from operator import itemgetter
from itertools import groupby
from functools import partial


def get_gist(path, version=3, public=True):
    """Calculate gist from directory.

    path:
        Path to directory to be summarized.
    version:
        Gist version to be used, 3 or 5.
    public_only:
        If True, only public gist will be calculated.

    Returns:
        Gist string.
    """
    if not path.endswith('/'):
        path += '/'

    files = sorted(os.listdir(path))
    if not public:
        files = [f for f in files if not f.startswith('.')]
    if not files:
        return None
    return hashlib.md5(path).hexdigest() + ''.join(files)


class _FileSet(object):
    def __init__(self, files):
        self._files = list(files)
        self._files.sort()

