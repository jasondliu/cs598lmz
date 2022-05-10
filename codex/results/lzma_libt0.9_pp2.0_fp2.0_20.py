import lzma
lzma.LZMADecompressor.get_unused_data = lambda x : b''

from .archives import extract_arc_lzma
from . import archives
from . import formatter

@register_handler('.pak')
def handle_pak(stream, verbose=False):
    # TODO: test
    # TODO: do we want to unpack these?
    stream.seek(0)
    header = stream.read(6)
    if header != b'TOMTOM':
        raise Exception('no magic "TOMTOM" string')
    version, toc, flags = struct.unpack('<iii', stream.read(12))
    flags = collections.OrderedDict()
    if version == 4:
        if verbose: print('reading new pak format')
        flags['unknown1'] = toc & 3
        flags['is_lzma'] = toc & 4
        flags['is_gz'] = toc & 8
        flags['is_zip'] = toc == 16
        flags['is_arc'] = toc ==
