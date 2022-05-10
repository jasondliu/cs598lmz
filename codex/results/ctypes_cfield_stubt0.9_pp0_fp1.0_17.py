import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
import six

class CFieldType(object):
    """
    Represents the type ctypes.ctypes.CField.
    """

    def __init__(self, field, type_name, type_class, count=1):
        self.field, self.type_class, self.count = field, type_class, count
        if not isinstance(type_name, six.string_types):
            raise ValueError('type_name must be a string')
        self.type_name = type_name

    def bin_format(self, idx):
        if self.count == 1:
            return "<{}{}{}".format(self.type_name, idx, self.field._type_)
        else:
            return "<{}{}{}".format(self.type_name, idx, self.field._type_ * self.count)

class LVecType(object):
    """
    Represents the type numpy.core.records.LVecType.
    """

    def __init__(self, field, type_name, type_class
