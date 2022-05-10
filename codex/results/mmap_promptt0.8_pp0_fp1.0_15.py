import mmap
# Test mmap.mmap
mmap.mmap(0,16384,mmap.MAP_SHARED,mmap.PROT_READ)


import ctypes
# Test ctypes.memset
ctypes.memset(0,0,16384)


import zlib
# Test zlib.crc32
zlib.crc32(b'data',0)


import _multiprocessing
# Test _multiprocessing.SemLock.acquire
_multiprocessing.SemLock.acquire(0)

# Test _multiprocessing.Connection.send
_multiprocessing.Connection.send(0,b'data',0)

# Test _multiprocessing.PipeConnection.recv_bytes
_multiprocessing.PipeConnection.recv_bytes(0,0)

# Test _multiprocessing.PipeConnection.send_bytes
_multiprocessing.PipeConnection.send_bytes(0,b'data',0)

# Test _multiprocessing.close
_mult
