import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import pytest
from pytest import raises
from hypothesis import given, assume
from hypothesis.strategies import from_type, one_of, lists, integers, text, binary, none
from hypothesis.database.formats import PickleFormat

from blastula import (
    new,
    fork,
    sleep,
    spawn,
    key,
    store,
    get,
    wait,
    wait_all,
    wait_any,
    wait_for,
    wait_for_all,
    wait_for_any,
    accept,
    wait_accept,
    close,
    process,
    ProcessClosed,
    ConnectionClosed,
    ConnectionSendClosed,
)

pytestmark = pytest.mark.unix


def test_new():
    p = new()
    assert p is not None
    assert p.parent is None
    assert p.children == []
    assert p.key is None

    p2 = new(p)
