import weakref
from _weakrefset import WeakSet
from typing import Optional, Type

from ._utils import is_async_gen, is_coroutine_function, is_coroutine_function_or_method

from ._remote import _get_method_name
from ._remote._remote_method import RemoteMethod
from ._remote._remote_property import RemoteProperty
from ._remote._remote_value import RemoteValue
from ._remote._remote_function import RemoteFunction
from ._remote._remote_class_method import RemoteClassMethod
from ._remote._remote_static_method import RemoteStaticMethod
from ._remote._remote_class import RemoteClass
from ._remote._remote_module import RemoteModule
from ._remote._remote_package import RemotePackage
from ._remote._remote_object import RemoteObject
from ._remote._remote_super import RemoteSuper
from ._remote._remote_partial import RemotePartial
from ._remote._remote_class_property import RemoteClassProperty
from ._remote._remote_import import RemoteImport
from ._remote._remote_builtin_function import RemoteBuiltinFunction
from ._remote._remote_builtin_method import RemoteBuiltinMethod

