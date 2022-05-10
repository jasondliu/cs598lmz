import io
# Test io.RawIOBase implements read, readinto, readall, write,
# seek and tell.
from io import RawIOBase
import os
from os import SEEK_CUR, SEEK_SET, SEEK_END
from io import open
