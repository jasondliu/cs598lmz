import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(
#   lambda x: -x)(5) == -5

# TODO(pts): Use ctypes.Structure and ctypes.CFUNCTYPE.

# --- struct dev_name_t.

# /usr/include/linux/major.h
MAJOR_SCSI_GENERIC = 21

# /usr/include/linux/kdev_t.h
def _MAJOR(dev):
  return (dev >> 8) & 0xfff

def _MINOR(dev):
  return (dev & 0xff) | ((dev >> 12) & 0xfff00)

def _MKDEV(ma, mi):
  return (ma << 8) | (mi & 0xff) | ((mi & 0xfff00) << 12)

class struct_dev_name_t(object):

  """Represents struct dev_name_t.

  Attributes:
    dev, sg_id: As in struct dev_name_t.
  """

  __slots__ = ('dev
