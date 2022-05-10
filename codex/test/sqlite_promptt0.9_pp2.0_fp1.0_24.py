import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')


# test cffi
from cffi import FFI


def export_to_module(filename):
    temp = sys.stdout
    code = open(filename, 'w')
    sys.stdout = code


def import_from_module(filename, t):
    # sys.path.append(os.path.abspath(filename[:-3]))
    # print(filename)
    if filename[:-3].startswith('./'):
        new_file = filename[3:-3]
    else:
        new_file = filename[:-3]
    # print(new_file)
    # linux only
    os.system('/usr/bin/ctags -x --fields=K --c-kinds=p ' + new_file + ' > .codes')
    # os.system('/usr/bin/ctags -x --fields=K --c-kinds=p ' + new_file + ' > ' + new_file + '.codes')
    # windows only
    # os.system('ctags -x
