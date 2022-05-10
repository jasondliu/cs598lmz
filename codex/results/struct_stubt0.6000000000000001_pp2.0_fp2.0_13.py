from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# test_stringio.py
from StringIO import StringIO
f = StringIO()
f.write('hi there')
f.seek(0)
f.read()

# test_struct.py
from struct import Struct
s = Struct('i')
s.pack(1)

# test_types.py
from types import FunctionType, ClassType, ModuleType, NoneType, \
    BuiltinFunctionType, BuiltinMethodType, MethodType, \
    CodeType, TracebackType, FrameType, SliceType, XRangeType, \
    DictProxyType, NotImplementedType, GetSetDescriptorType, \
    MemberDescriptorType, GeneratorType, EllipsisType

# test_warnings.py
from warnings import warn
warn('hello')

# test_weakref.py
from weakref import ref
def f(): pass
r = ref(f)
r()

# test_zipimport.py
from zipimport import zipimporter
zi = zipimporter
