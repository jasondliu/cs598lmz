import io
class File(io.RawIOBase):
    """An enhanced version of Python's built-in file object.

    ***For now, just an alias of io.RawIOBase***
    
    This behaves similarly to Python's built-in file object,
    but with a few differences:

    - The 'mode' argument can be used to create a new file,
      or to append to an existing file.
    - The 'mode' argument can be used to create a temporary
      file object for use with context managers or 'with'
      statements.

    Not implemented in this version:
    
    - Codes determined by the operating system (such as
      'b' on Windows) are auto-appended to a mode string.
      (I may change this since it's considered good practice
      to include 'b' on all systems.)

    - Temporary files have no auto-naming mechanism (which
      is good, because the Python built-in file objects'
      auto-naming is buggy on Windows).
    
    - Memory-mappable files are supported, but not yet added.
    """
    def __init__(self, filename=None, mode='r',
