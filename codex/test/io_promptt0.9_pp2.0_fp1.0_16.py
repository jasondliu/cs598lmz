import io
# Test io.RawIOBase on Windows to ensure that non-inheriting descendants can
# be used as raw I/O.
# On Windows, all modules that depend on the _winapi module should be imported
# before importing the _multiprocessing module.
from multiprocessing.dummy import Pool
