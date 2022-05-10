import weakref

from vfs_s3fs import S3FS

from . import util
from .util import Serializable, log_debug, log_error, log_info, log_warn

__all__ = [
    'S3BackedFileSystem',
    'S3BackedFile',
    'S3BackedFileDescriptor',
    'S3BackedFileStat',
    'S3BackedFileSystemStat',
    'S3BackedDirectory',
    'S3BackedDirectoryEntry',
]

# The max size of an individual object in S3.
MAX_OBJECT_SIZE = 5 * 1024 * 1024 * 1024

# The max size of a single multipart upload.
MAX_MULTIPART_SIZE = 5 * 1024 * 1024 * 1024

# The max number of parts in a multipart upload.
MAX_PARTS = 10000

# The max size of a single chunk of data to read/write.
CHUNK_SIZE = 5 * 1024 * 1024

# The number of chunks to buffer at once.
CHUNK_BUFFER = 10

#
