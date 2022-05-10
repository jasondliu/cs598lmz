import _struct
# from .utils import *
from .utils import *
from .calc_md5sum import md5sum
# from . import md5sum


def parse_vdi_header(fname):
    """Parses VDI Header from VDI file.
    :param fname: VDI filename
    :returns: dictionary, containing parsed elements of VDI header
    """
    h = {}
    f = open(fname, 'rb')
    # f = open(bytes(fname, encoding='utf8'), 'rb')
    s = _struct.Struct(">III")
    (h["image_type"], h["header_version"], h["image_flags"]) = s.unpack(f.read(s.size))
    s = _struct.Struct(">L")
    h["image_description"] = unpack_string(f.read(s.size), byte_order="big")
    s = _struct.Struct(">LLLLLL")
    (
        h["image_offset"],
        h["image_blocks"],
        h["block_size"],
