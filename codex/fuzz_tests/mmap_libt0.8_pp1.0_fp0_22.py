import mmap
import fcntl


class Mock(object):

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ('__file__', '__path__'):
            return '/dev/null'
        elif name[0] == name[0].upper():
            mockType = type(name, (), {})
            mockType.__module__ = __name__
            return mockType
        else:
            return Mock()

MOCK_MODULES = ['_caffe', 'h5py', 'numpy', 'scipy']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()

import mace
import mace.proto.mace_pb2 as mace_pb
from mace.python.tools.converter_tool import ConverterTool
from mace.python.tools.transform_util
