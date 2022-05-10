import ctypes
ctypes.cast(ctypes.c_void_p(0), ctypes.c_char_p).value = '\0'

try:
    import elftools
except ImportError:
    print('python-elftools is required to run this script, please install'
          ' it first')
    sys.exit(1)

from elftools.elf.elffile import ELFFile


def get_abs_path_from_dir(dirpath, relpath):
    """ Return the absolute path of relpath relative to dirpath.

    >>> import os
    >>> dirpath = os.path.dirname(__file__)
    >>> get_abs_path_from_dir(dirpath, 'test.py')
    '/absolute/path/to/test.py'
    """
    abspath = os.path.join(dirpath, relpath)
    if not os.path.isabs(abspath):
        abspath = os.path.abspath(abspath)
    return abspath


class ElfFile(object):
    """ Represents an ELF file.
