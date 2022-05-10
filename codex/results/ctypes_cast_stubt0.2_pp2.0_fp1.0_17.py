import ctypes
ctypes.cast(0, ctypes.py_object)

# ___________________________________________________________________________
# Exceptions

class Error(Exception):
    pass

class InterfaceError(Error):
    pass

class DatabaseError(Error):
    pass

class DataError(DatabaseError):
    pass

class OperationalError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class InternalError(DatabaseError):
    pass

class ProgrammingError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass

# ___________________________________________________________________________
# DB API 2.0 Module Methods

def connect(dsn, user=None, password=None, host=None, database=None,
            port=None, unix_sock=None, conv=None, use_unicode=None,
            client_flag=0, cursorclass=Cursor, init_command=None,
            connect_timeout=None, ssl=None, read_default_file=None,
            read_default_group=None, compress=None, named_pipe=None,
            no
