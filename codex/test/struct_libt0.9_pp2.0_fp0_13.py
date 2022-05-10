import _struct
from ctypes import util
from ctypes import wintypes

from protos import big_file_pb2 as big_file
from protos import bytes_metadata_pb2 as bytes_metadata

_LIBC = ctypes.CDLL(util.find_library('c'))
_libc_lock_t = ctypes.c_char * 20
_libc_pthread_rwlock_t = ctypes.c_char * 24


@utils.contextmanager
def _ReadGlobalMutex(mutex):
  """Utility function to acquire & lock a pthread rwlock.

  Args:
    mutex: The mutex to be locked.
  """
  _LIBC.pthread_rwlock_rdlock(
      ctypes.byref(mutex))
  try:
    yield
  finally:
    _LIBC.pthread_rwlock_unlock(
        ctypes.byref(mutex))


