import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)
# For pip:
# python setup.py bdist_wheel
# pip install ./dist/sqlite3-shared-0.0.1-py3-none-any.whl
# pip install --user ./dist/sqlite3-shared-0.0.1-py3-none-any.whl

# For local:
# python setup.py install --user
# python3 -m sqlite3_shared

# For Linux:
# gcc -shared -o sqlite3-shared.so -fPIC sqlite3-shared.c
# LD_PRELOAD=./sqlite3-shared.so sqlite3

# For Mac:
# gcc -shared -o sqlite3-shared.dylib -fPIC sqlite3-shared.c
# DYLD_INSERT_LIBRARIES=./sqlite3-shared.dylib DYLD_FORCE_FLAT_NAMESPACE=1 sqlite3

from setuptools import setup, find_packages

setup(
    name
