import lzma
lzma = lzma.lzma
import os
import re
import tempfile
import xml.etree.ElementTree as ET


if sys.version_info[0] < 3:
    from cStringIO import StringIO
    from urllib import urlretrieve
else:
    from io import StringIO
    from urllib.request import urlretrieve

import numpy as np

from .parsers import (
    _parse_v4_parameter_table, _parse_v4_special_functions,
    _parse_v4_svn_info, parse_v4_filter_table, _parse_v4_compilation_info,
    _parse_v4_bibliography
)
from .version import version as __version__
from . import (
    _datalad_doc_urls, _license_doc_urls,
    _get_datalad_crawl_version, _get_license_crawl_version
)


_logger = logging.getLogger('datalad_crawler_datasets')
_
