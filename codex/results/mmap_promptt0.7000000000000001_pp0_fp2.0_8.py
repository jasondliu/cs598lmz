import mmap
# Test mmap.mmap size
from os import SEEK_SET
import ctypes

from util.ByteUtil import ByteUtil
from util.FileUtil import FileUtil

from util.LogUtil import LogUtil

class MMapUtil:
    """
    mmap utility class
    """

    log = None
    file_util = None
    byte_util = None

    def __init__(self):
        """
        init
        """
        self.log = LogUtil().get('mmap')
        self.file_util = FileUtil()
        self.byte_util = ByteUtil()

    def get(self, file_name, file_size=None, offset=0, length=0, access=mmap.ACCESS_WRITE):
        """
        mmap object
        """
        if file_size is None:
            file_size = self.file_util.get_file_size(file_name)

        with open(file_name, 'r+b') as file:
            if length == 0:
                self.log.info('mm
