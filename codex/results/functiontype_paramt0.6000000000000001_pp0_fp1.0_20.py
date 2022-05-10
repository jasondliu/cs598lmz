from types import FunctionType
list(FunctionType(lambda x:x,globals(),'lambda_function'))

from types import LambdaType
list(LambdaType(lambda x:x,globals(),'lambda_function'))

from types import MethodType
list(MethodType(lambda x:x,globals(),'lambda_function'))

from types import ModuleType
list(ModuleType('name', 'doc'))

from types import MappingProxyType
list(MappingProxyType({'a':'b'}))

from types import SimpleNamespace
list(SimpleNamespace(name = 'value'))

from types import TracebackType
list(TracebackType(frame = 1, lasti = 2, lineno = 3))

from types import _collections_abc
list(_collections_abc.Mapping)
list(_collections_abc.Mapping.__abstractmethods__)

from types import _weakref
list(_weakref.ReferenceType)
list(_weakref.ReferenceType.__abstractmethods__)

from types import _weakrefset
list(_weakref
