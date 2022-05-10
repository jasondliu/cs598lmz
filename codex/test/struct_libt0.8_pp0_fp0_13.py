import _struct
from ctypes import *
from util import get_bytes, get_string, get_dword, get_word, get_short, get_int, get_double
from util import convert_bytes_to_hex

class DataReader(object):
    def __del__(self):
        self.close()

    def __init__(self, fixture_id, filename):
        self.m_handle = 0
        self.m_fixture_id = fixture_id
        self.m_filename = filename
        self.m_row = []

    def open(self):
        self.m_handle = os.open(self.m_filename, os.O_RDONLY)

    def close(self):
        os.close(self.m_handle)

    def read_header(self):
        header = os.read(self.m_handle, 14)
        if header[0:8] != b'USEMSr2\x01':
            raise Exception("Bad file header")
        self.m_fixture_id = get_int(header[8:12])
