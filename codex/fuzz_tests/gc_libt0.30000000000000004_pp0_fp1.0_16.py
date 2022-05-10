import gc, weakref
from collections import defaultdict
from functools import partial
from itertools import islice, chain
from operator import itemgetter
from threading import Lock

from six import iteritems, itervalues
from six.moves import xrange

from . import _compat as six
from . import _compat, _utils, _iterators, _compression, _compat_pickle
from . import _indexed_gzip as igzip
from . import _htslib
from . import _vcf_parser, _vcf_helpers
from . import _tabix_helpers
from . import _interval_tree
from . import _bgzf

from ._compat import (
    basestring,
    BytesIO,
    get_range_string,
    is_integer,
    is_string,
    is_text,
    is_binary,
    is_bytes,
    is_file,
    is_file_like,
    is_file_path,
    is_file_like_or_path,
    is_file_
