import lzma
lzma_open = lzma.open
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

from .compat import PY3, text_type

# TODO: split this into a separate module (and ensure no refs to DBLog)
import struct

class Common(object):

    # for logging
    LOG_CURRENT = 11
    LOG_PREVIOUS = 12
    LOG_NONE = 0
    LOG_OPEN_FAIL = -1
    LOG_READ_FAIL = -2
    LOG_TIMESTAMP_FAIL = -3
    LOG_RECOVER_FAIL = -4
    LOG_TRUNCATED = -5
    LOG_INCORRECT_SIZE = -6
    LOG_WRITE_FAIL = -7

    def __init__(self, conf, logURLPrefix, db_home, db_name, db_ext, db_mode, db_factory, db_isolation_level, db_rw_isolation_level,
