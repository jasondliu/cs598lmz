import mmap
import threading

from ctypes import *

# typedef struct {
#   uint32_t magic;
#   uint32_t size;
#   uint64_t offset;
#   uint64_t timestamp;
#   uint32_t type;
#   uint32_t flags;
#   uint64_t pid;
#   uint64_t tid;
#   char name[16];
#   char format[64];
#   uint8_t data[0];
# } ATRACE_PACKET;

class ATRACE_PACKET(Structure):
    _pack_ = 1
    _fields_ = [
        ("magic", c_uint32),
        ("size", c_uint32),
        ("offset", c_uint64),
        ("timestamp", c_uint64),
        ("type", c_uint32),
        ("flags", c_uint32),
        ("pid", c_uint64),
        ("tid", c_uint64),
        ("name", c_char * 16),
        ("format", c
