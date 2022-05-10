import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import config
from . import utils
from . import log
from . import errors
from . import __version__

from .utils import (
    get_file_path,
    get_file_name,
    get_file_ext,
    get_file_size,
    get_file_mtime,
    get_file_ctime,
    get_file_atime,
    get_file_mode,
    get_file_uid,
    get_file_gid,
    get_file_inode,
    get_file_dev,
    get_file_nlink,
    get_file_rdev,
    get_file_blksize,
    get_file_blocks,
    get_file_flags,
    get_file_gen,
    get_file_type,
    get_file_content,
    get_file_content_hash,
    get_file_content_hash_type,
    get_file_content_hash_encoding,
    get_file
