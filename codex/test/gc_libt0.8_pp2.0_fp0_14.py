import gc, weakref
import struct, sys
from fcntl import ioctl
from os import open, O_RDWR, O_SYNC
from select import select
