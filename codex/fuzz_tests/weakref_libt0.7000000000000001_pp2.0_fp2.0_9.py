import weakref

import pytest

from pypy.interpreter.error import OperationError
from pypy.module.cpyext.test.test_api import BaseApiTest, raises_w
from pypy.module.cpyext.test.test_cpyext import AppTestCpythonExtensionBase
from pypy.module.cpyext.typeobject import (
    PyTypeObjectPtr, PyTypeObject, make_typedescr)
from pypy.module.cpyext.pyobject import PyObject, make_ref, from_ref
from pypy.module.cpyext.api import (
    cpython_api, PyObjectFields, PyObjectStruct, build_type_checkers)
from pypy.module.cpyext.pyerrors import PyErr_Occurred
from pypy.module.cpyext.methodobject import py_method_new
from pypy.module.cpyext.object import PyObject_Repr
from pypy.module.cpyext.pyobject import decref, incref
from pypy
