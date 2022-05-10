import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
with sqlite3.connect(':memory:') as db:
    pass
# Test sqlite3.Cursor
cursor = sqlite3.Cursor
# Test sqlite3.Connection
connection = sqlite3.Connection
# Test sqlite3.Row
row = sqlite3.Row
# Test sqlite3.Error
error = sqlite3.Error
# Test sqlite3.Warning
warning = sqlite3.Warning
# Test sqlite3.DatabaseError
database_error = sqlite3.DatabaseError
# Test sqlite3.OperationalError
operational_error = sqlite3.OperationalError
# Test sqlite3.IntegrityError
integrity_error = sqlite3.IntegrityError
# Test sqlite3.ProgrammingError
programming_error = sqlite3.ProgrammingError
# Test sqlite3.NotSupportedError
not_supported_error = sqlite3.NotSupportedError
# Test sqlite3.Binary
binary = sqlite3.Binary(b'foo')
# Test sqlite3.register_adapter
sqlite3.register
