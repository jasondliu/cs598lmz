import _struct
from collections import OrderedDict
from . import error
from .serializer import Serializer

class Packer(object):
    def pack(self, obj):
        raise NotImplementedError()

    def unpack(self, data):
        raise NotImplementedError()

class GenPacker(Packer):
    def __init__(self, struct_format=None, **kwd):
        self.struct_format = struct_format
        self.pack_list = OrderedDict()
        self.unpack_list = OrderedDict()
        self.pack_list["serialize"] = Serializer()
        self.unpack_list["serialize"] = Serializer()

class TemplateError(RuntimeError):
    def __init__(self, msg, tag=""):
        super(TemplateError, self).__init__(msg, tag)

