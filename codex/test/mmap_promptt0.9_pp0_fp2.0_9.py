import mmap
# Test mmap.mmap(0, 1 << 31, "shared", mmap.MAP_ANONYMOUS)

# Author: jrnetdev
# License: MIT
# Source: https://gist.github.com/jrnetdev/b8cfc7f622b34e05f3e3

# Constants for specifying sync accessing mode.
SYNC_UNSYNCRONIZE = -1
SYNC_SYNCRONIZE = 0
SYNC_CACHED = 1


class SharedMemory:
    class __SharedMemory:

        def __init__(self, init=None, initCapacity=0, accessMode=mmap.ACCESS_WRITE, filename=None):
            self.__accessMode = accessMode
            self.__syncAccess = SYNC_SYNCRONIZE
            self.__filename = filename
            self.__mem = None
            self.__memCapacity = 0
            self.__memSize = 0

