import io
class File(io.RawIOBase):
  def __init__(self, f):
    self.f = f
  def seekable(self):
    return True
  def tell(self):
    return self.f.tell()
  def seek(self, offset, whence=io.SEEK_SET):
    if whence == io.SEEK_CUR:
      offset += self.f.tell()
    self.f.seek(offset)
  def readinto(self, b):
    n = self.f.readinto(b)
    return n
  def read(self, n=-1):
    return self.f.read(n)

from dulwich.repo import Repo
from dulwich.objects import (
  Blob,
)

from . import cache

from .util.git import (
  execute,
  pack_into,
  unpack_from,
  )
from .util import fs
from .util import lru
from . import objects
from . import types
from . import schema


class Repository(Repo):
  Schema = types.Repository

