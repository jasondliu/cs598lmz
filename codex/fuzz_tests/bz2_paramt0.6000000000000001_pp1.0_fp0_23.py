from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self, _: self.decompress(b'')  # https://stackoverflow.com/questions/18387307/python-bz2-decompressor-invalid-data-stream

from collections import defaultdict
from datetime import datetime
from gzip import GzipFile
from hashlib import md5
from io import BytesIO

from . import (
    config,
    exceptions,
    utils,
)


__all__ = [
    'get_public_key',
    'get_repo_key',
    'get_signature',
]


def get_signature(mirror, repo, arch, keyring_file):
    """Return signature for given repo, arch, and package"""
    if mirror is None or not mirror:
        raise exceptions.MirrorNotFound("mirror is None or empty")

    sig_path = config.SIGNATURE_PATH.format(
        mirror=mirror,
        repo=repo,
        arch=arch,
    )

    key_path = config.KEY_PATH.format(
