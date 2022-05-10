import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import builtins
import re
import time
import platform

# This is a hack to get python to actually run the functions
# in the module as if they were run as the top level
if __name__ == '__main__':
    raise Exception('This program cannot be run in DOS mode.')

# This is a hack to get python to actually run the functions
# in the module as if they were run as the top level
if __name__ == '__main__':
    raise Exception('This program cannot be run in DOS mode.')

# Function Library
def func_main():
    if(os.path.isfile(database_name)):
        if(os.path.isfile(settings_name)):
            func_readsettings()
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
            func_readdb()
            print('- - - - - - - - - - -
