import _struct

from . import _common
from . import _compression
from . import _constants
from . import _errors
from . import _util
from . import _version


class Reader(object):
  """A class for reading an Ogg stream."""

  def __init__(self, file_obj, serial_number=None,
               ignore_errors=False,
               ignore_first_page=False,
               ignore_checksum=False,
               ignore_version=False,
               ignore_serial_number=False,
               ignore_header_types=False,
               ignore_first_page_header_types=False,
               ignore_first_page_header_type_sequence=False,
               ignore_first_page_header_type_continuation=False,
               ignore_first_page_header_type_bos=False,
               ignore_first_page_header_type_eos=False,
               ignore_first_page_header_type_granule_position=False,
               ignore_first_page_header_type_bitstream_serial_number=False,
              
