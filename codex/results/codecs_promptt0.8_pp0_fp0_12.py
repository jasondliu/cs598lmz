import codecs
# Test codecs.register_error('test-encode', test_encode)
from functools import partial

from typing import *

from . import *
from .utils import *
from .subtitle import *
from .subtitle.subtitle_timestamp import *

from .subtitle.subtitle_list import SubtitleList

from .subtitle.subtitle_file_codec import SubtitleFileCodec

from .subtitle.subtitle_file_formats import SRT

from .subtitle.subtitle_list_codec import SubtitleListCodec



class Config():
    pass


config = Config()

config.encoding_fallback = ['cp1251', 'utf-8-sig', 'utf-8', 'utf-16']
config.encoding_fallback_decode_ignore = []
config.encoding_fallback_decode_replace = []

config.encoding_wrong_byte_sequence = 'replace'
config.encoding_wrong_byte_sequence_decode_replace = []
config.encoding_wrong_byte_sequence_decode_
