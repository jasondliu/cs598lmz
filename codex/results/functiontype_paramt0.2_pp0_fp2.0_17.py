from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'func'))

# code object
from types import CodeType
list(CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b''))

# method-wrapper object
from types import MethodWrapperType
list(MethodWrapperType(lambda x: x, None, None))

# wrapper descriptor object
from types import WrapperDescriptorType
list(WrapperDescriptorType(lambda x: x))

# method-descriptor object
from types import MethodDescriptorType
list(MethodDescriptorType(lambda x: x))

# class method-descriptor object
from types import ClassMethodDescriptorType
list(ClassMethodDescriptorType(lambda x: x))

# member descriptor object
from types import MemberDescriptorType
list(MemberDescriptorType(lambda x: x))

# getset-descriptor object
from types import GetSetDescriptorType
list(GetSetDescriptorType(lambda x: x, lambda x: x, lambda x: x
