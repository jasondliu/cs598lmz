import gc, weakref, datetime

from fsspec.utils import stringify_paths
from fsspec.core import _fs_opener
from fsspec.implementations.base import REGISTRY as registry
from fsspec.spec import AbstractFileSystem

from .core import _transform, _infer_storage_options
from .utils import tokenize, MODE_BINARY, _make_meta
from .local import LocalFileSystem
from .dropbox import DropboxFileSystem
from .gcs import GCSFileSystem
from .http import HTTPFileSystem
from .s3 import S3FileSystem
from .ftp import FTPFileSystem
from .zip import ZipFileSystem
from .webhdfs import WebHDFS
from .sftp import SFTPFileSystem
from .ssh import SSHFileSystem

def open(path, mode='rb', storage_options=None, **kwargs):
    """Open file for reading or writing

    Parameters
    ----------
    path: str or File-like
        If a string, path to open. If an open file-like, use as is. Use

