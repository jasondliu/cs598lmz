import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import csv
import cStringIO


"""
Write a function that takes as its input a string, and returns TRUE if
the string represents a valid identifier in lua.
For purposes of this exercise, you can assume a valid Lua identifier is the same thing
as a valid Python indentifier (e.g., "for", "while", "+", "-", etc. are valid Python
identifiers and therefore valid Lua idents).
"""

def isLegalLuaIdent(ident):
    try:
        compile(ident, '<string>', 'eval')
    except SyntaxError as err:
        # print "got a syntax exception", err
        return False
