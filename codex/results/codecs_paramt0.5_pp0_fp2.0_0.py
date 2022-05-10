import codecs
codecs.register_error('strict', codecs.ignore_errors)

from collections import defaultdict
from collections import OrderedDict

from . import utils
from . import config
from . import vcf
from . import snp
from . import ped
from . import log
from . import __version__ as version

from .utils import (
    get_file_type,
    get_file_format,
    get_file_extension,
    get_file_handle,
    get_file_name,
    get_file_path,
    get_file_directory,
    get_file_basename,
    get_file_header,
    get_file_iterator,
    get_file_content,
    get_file_size,
    get_file_md5,
    get_file_sha1,
    get_file_sha256,
    get_file_sha512,
    get_file_content_md5,
    get_file_content_sha1,
    get_file_content_sha256,
    get_file_content_sha512,
   
