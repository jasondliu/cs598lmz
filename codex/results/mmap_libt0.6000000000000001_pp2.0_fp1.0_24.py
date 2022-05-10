import mmap
from operator import itemgetter
from functools import partial

from . import _util
from . import _map

from . import _common
from . import _compat
from . import _parse
from . import _sort
from . import _sort_merge


_logger = logging.getLogger(__name__)


def _read_chunk(f, chunk_id):
    f.seek(chunk_id * _common.CHUNK_SIZE)
    chunk_data = f.read(_common.CHUNK_SIZE)
    if len(chunk_data) != _common.CHUNK_SIZE:
        raise ValueError('Truncated chunk')
    return chunk_data


class _Chunk(object):
    """Represents a chunk of data."""

    def __init__(self, data, index, next_chunk_id):
        self.data = data
        self.index = index
        self.next_chunk_id = next_chunk_id

    def __repr__(self):
        return '_Ch
