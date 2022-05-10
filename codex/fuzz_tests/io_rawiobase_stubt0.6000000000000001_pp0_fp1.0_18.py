import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def readall(self):
        return self.f.read()
    def close(self):
        self.f.close()

from . import http
import os
from . import __main__
from . import builtin
from . import __loader__
from . import __builtin__
from . import __future__
from . import __spec__
from . import _sitebuiltins
from . import _sysconfigdata_m_linux_x86_64-linux-gnu
from . import _sitebuiltins
from . import _sysconfigdata_m_linux_x86_64-linux-gnu
from . import _sitebuiltins
from . import _sysconfigdata_m_linux_x86_64-linux-gnu
from . import _sitebuiltins
from . import _sysconfigdata_m_linux_x86_64-linux-gnu
from . import _sitebuiltins
from . import _sysconfigdata_m_
