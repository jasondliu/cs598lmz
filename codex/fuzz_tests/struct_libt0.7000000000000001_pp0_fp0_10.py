import _struct
from _multibytecodec import _make_codec

_mbcs_decoder = _make_codec('mbcs', _codecs_mbcs.getcodec)
_mbcs_encoder = _make_codec('mbcs', _codecs_mbcs.getcodec)


class Codec(_codecs_cn.Codec):
    encode = _mbcs_encoder
    decode = _mbcs_decoder


class IncrementalEncoder(_codecs_cn.IncrementalEncoder):
    __qualname__ = 'IncrementalEncoder'
    codec = _mbcs_codec


class IncrementalDecoder(_codecs_cn.IncrementalDecoder):
    __qualname__ = 'IncrementalDecoder'
    codec = _mbcs_codec


class StreamWriter(Codec, _codecs_cn.StreamWriter):
    __qualname__ = 'StreamWriter'
    codec = _mbcs_codec


class StreamReader(Codec, _codecs_cn.StreamReader):
    __qual
