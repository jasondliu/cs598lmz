import _struct

from global_vars import *
from structs import *
from utils import *

from pprint import pprint

def unpack(data, size_to_read, offset, format):
    return _struct.unpack_from(format, data, offset)[0], offset + size_to_read

def unpack_string(data, size_to_read, offset, format):
    format += str(size_to_read) + 's'
    return _struct.unpack_from(format, data, offset)[0], offset + size_to_read

def unpack_list(data, size_to_read, offset, format):
    format += str(size_to_read / 4) + 'i'
    return _struct.unpack_from(format, data, offset), offset + size_to_read

class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name, 'rb') as file_obj:
            self.data = file_obj.read
