import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# Test sqlite3.connect()

def test_connect():
    try:
        con = sqlite3.connect(":memory:")
        assert con.total_changes == 0
    finally:
        con.close()

def test_connect_factory():
    def my_factory(*args, **kwargs):
        return sqlite3.connect(*args, **kwargs)
    try:
        con = sqlite3.connect(":memory:", factory=my_factory)
        assert con.total_changes == 0
    finally:
        con.close()

def test_connect_factory_with_kwargs():
    def my_factory(**kwargs):
        return sqlite3.connect(**kwargs)
    try:
        con = sqlite3.connect(":memory:", factory=my_factory)
        assert con.total_changes == 0
    finally:
        con.close()

def test_connect_factory_with_args():
    def my_factory(*args):
        return sqlite3
