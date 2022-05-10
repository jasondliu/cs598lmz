import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from lxml import etree
import requests

from . import config
from . import constants
from . import exceptions
from . import utils
from . import xbmc_vfs
from . import xbmc_vfs_file
from . import xbmc_vfs_url
from . import xbmc_vfs_zip
from . import xbmc_vfs_rar
from . import xbmc_vfs_7z
from . import xbmc_vfs_tar
from . import xbmc_vfs_gzip
from . import xbmc_vfs_bz2
from . import xbmc_vfs_lzma
from . import xbmc_vfs_xz
from . import xbmc_vfs_lz4
from . import xbmc_vfs_zstd
from . import xbmc_vfs_lzo
from . import xbmc_vfs_lz4
