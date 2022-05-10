import _struct

from .constants import *
from . import io
from . import read
from . import write
from . import metadata
from . import metadata_categories
from . import import_icoon
from . import export_icoon
from . import cleanup


def _get_meta_category_by_id(meta_category_id):
    return metadata_categories.META_CATEGORIES.get(meta_category_id, "")


def _convert_meta_timestamp(meta_timestamp):
    timestamp = meta_timestamp & 0x7FFFFFFF
    month = (timestamp >> 5) & 0x0F
    day = timestamp & 0x1F
    year = timestamp >> 11
    return "%04d-%02d-%02d" % (2000 + year, month, day)


def _convert_meta_bool(meta_bool):
    return bool(meta_bool & 0x02)

