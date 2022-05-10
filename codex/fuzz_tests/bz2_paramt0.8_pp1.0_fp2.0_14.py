from bz2 import BZ2Decompressor
BZ2Decompressor()

class FileType(IntEnum):
    UNKNOWN = 0
    TAR = 1
    BZ2 = 2


class DupFinder:
    """A tool for find duplicated files"""
    def __init__(self,
                 debug=False,
                 log_level=logging.ERROR):
        """Initialize the DupFinder
        Args:
            debug: True to print debug information
            log_level: logging level
        """
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)
        self.debug = debug

        self.file_list = []
        self.dup_list = []

    def add_file(self, file_name):
        """Add a file to the dup finder

        The file_name will not be added, if the file name is duplicated with
        an exsiting file.

        Args:
            file_name: the file name
        """
        if self.debug:
            self.logger.debug('Add file {}'.format(file_
