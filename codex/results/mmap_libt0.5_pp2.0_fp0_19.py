import mmap

from . import utils
from . import exceptions
from . import config

log = logging.getLogger(__name__)


class BaseFile(object):
    """
    Base File class.

    This class is not meant to be instantiated.
    """
    #: Default file extension for this file type
    extension = ''

    def __init__(self, filename):
        """
        :param filename: Path to the file.
        """
        self.filename = filename
        self.path = os.path.dirname(filename)
        self.basename = os.path.basename(filename)
        self.name, self.ext = os.path.splitext(self.basename)

        #: File size
        self.size = os.path.getsize(filename)

        self.is_new = not os.path.exists(self.filename)

        self._fd = None
        self._mm = None

    def __repr__(self):
        return '<{0} {1}>'.format(self.__class__.__
