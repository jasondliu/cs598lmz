import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
import pytest
# Test pytest.raises()
import sys

# Determine if running on Python 2 or Python 3
PY3 = sys.version_info >= (3, 0)


@pytest.mark.parametrize('uri', [
    'file:test.db?mode=ro',
    'file:test.db?mode=rw',
    'file:test.db?mode=rwc',
    'file:test.db?mode=memory',
    'file:test.db?mode=memory&cache=shared',
])
def test_connect(uri):
    conn = sqlite3.connect(uri)
    assert isinstance(conn, sqlite3.Connection)
    assert conn.closed == 0
    assert conn.total_changes == 0
    assert conn.in_transaction == 0
    assert conn.isolation_level == ''
    assert conn.row_factory is None

    conn = sqlite3.connect(uri, uri=True)
    assert isinstance(conn, sqlite3.Connection)
    assert conn.
