import lzma
lzma.CHECK_CRC32 = True

from . import const
from . import generic
# from . import android

logger = logging.getLogger(__name__)


class GenericParser(object):
    '''Implementation of parsing of generic file'''
    def __init__(self, filepath, **kwargs):
        self.partition_type = kwargs['partition_type']
        self.use_lzma = kwargs['use_lzma']
        self.keep_raw_data = kwargs['keep_raw_data']
        self.encryption = kwargs['encryption']
        self.format = kwargs['format']
        self.file = None
        self.filepath = filepath
        self.unpacked_filepath = os.path.join(os.path.dirname(self.filepath), 'unpacked_data.bin')
        self.data_dict = {}
        try:
            self.file = open(filepath, 'rb')
            if 'brom' in self.partition_type
