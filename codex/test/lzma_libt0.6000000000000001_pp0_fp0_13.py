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

