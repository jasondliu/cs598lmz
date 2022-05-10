import lzma
lzma.open = lzma.LZMAFile

import tarfile
import zipfile

from io import BytesIO
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import namedtuple
from functools import reduce

from . import config
from . import util

from .util import open_file
from .util import open_file_write
from .util import open_file_read
from .util import open_file_gzip
from .util import open_file_bz2
from .util import open_file_lzma
from .util import open_file_stdin
from .util import open_file_stdout
from .util import open_file_stdin_text
from .util import open_file_stdout_text
from .util import open_file_read_write
from .util import open_file_read_write_text
from .util import open_file_read_write_binary
from .util import open_file_read_binary
from .util import open_file_write_binary
from .util import open
