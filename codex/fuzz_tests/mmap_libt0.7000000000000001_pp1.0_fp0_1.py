import mmap
import datetime
import sys
import time

from . import common

#
# Section:
#

class Section(object):
    """
    Base class for sections.
    """
    def __init__(self, offset, size):
        self._offset = offset
        self._size = size


class SectionV1_0(Section):
    """
    Section for version 1.0.
    """
    def __init__(self, offset, size):
        super(SectionV1_0, self).__init__(offset, size)
        self._header_size = 0x100
        self._header_offset = 0x100
        self._data_size = 0x100
        self._data_offset = 0x200
        self._footer_size = 0x100
        self._footer_offset = 0x300
        self.header = None
        self.data = None
        self.footer = None

    def get_header(self):
        return self.header

    def get_data(self):
        return self.data

    def get
