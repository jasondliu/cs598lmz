import lzma
lzma.LZMA_PATH = 'C:\Program Files\7-Zip\7z.exe'

import re
import os
import subprocess
import shutil
from pathlib import Path

from . import config
from .file import File
from . import util

class Archive(File):
    """
    Class for handling archive files.

    Supported formats:
    7z, zip, rar, tar, tar.gz, tar.bz2, tar.xz, tar.lzma, tar.Z, tar.lz4,
    tar.lzop, tar.sz, tar.zst, tar.tzst, tar.snappy, tar.iso, tar.vhd,
    tar.vhdx, tar.vdi, tar.vmdk, tar.qcow, tar.qcow2, tar.btrfs, tar.cpio,
    tar.shar, tar.ar, tar.mtree, tar.warc, tar.xar, tar.mime, tar.lha,
    tar.lrzip, tar.lz4, tar
