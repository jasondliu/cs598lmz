import weakref

from . import _data, _midi, _util, _lib
from ._lib import ffi, lib

_allocs = set()

def _free_allocs():
    for ref in _allocs:
        ptr = ref()
        if ptr:
            lib.jack_ringbuffer_free(ptr)

atexit.register(_free_allocs)

def _free(ptr):
    if ptr:
        lib.jack_ringbuffer_free(ptr)

class RingBuffer(_lib._RingBuffer):
    '''A JACK FIFO ring buffer.

    See :c:type:`jack_ringbuffer_t` for documentation.

    '''
    def __init__(self, size):
        '''Create a ring buffer with size *size*.

        '''
        if size <= 0:
            raise ValueError('size must be greater than zero')
        ptr = lib.jack_ringbuffer_create(size)
        if not ptr:
            raise MemoryError()
        _allocs.add(weakref.ref(ptr, _free))
       
