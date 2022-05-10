import ctypes
ctypes.cast(0, ctypes.py_object)

import pytest

from pytestqt.qt_compat import qt_api
from pytestqt.qt_compat import _is_pytest_qt_api_1
from pytestqt.qt_compat import _is_pytest_qt_api_2
from pytestqt.qt_compat import _is_pytest_qt_api_2_plus
from pytestqt.qt_compat import _is_pytest_qt_api_3_plus


@pytest.mark.parametrize('qt_api_version, expected', [
    (1, True),
    (2, False),
    (3, False),
])
def test_is_pytest_qt_api_1(qt_api_version, expected):
    qt_api.pytest_qt_api_version = qt_api_version
    assert _is_pytest_qt_api_1() == expected


@pytest.mark.parametrize('qt_api_version, expected', [
    (1
