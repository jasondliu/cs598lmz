import weakref

import pytest

from pypy.interpreter.error import OperationError
from pypy.module.cpyext.test.test_api import BaseApiTest, raises_w
from pypy.module.cpyext.test.test_cpyext import AppTestCpythonExtensionBase
from pypy.module.cpyext.typeobject import (
    PyTypeObjectPtr, PyTypeObject, make_typedescr)
