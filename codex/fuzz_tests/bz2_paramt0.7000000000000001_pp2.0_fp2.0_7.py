from bz2 import BZ2Decompressor
BZ2Decompressor()

from _codecs import encode, decode, lookup, register

from _codecs_cn import getcodec, getincrementalencoder, getincrementaldecoder

from _codecs_hk import getcodec, getincrementalencoder, getincrementaldecoder

from _codecs_iso2022 import getcodec, getincrementalencoder, getincrementaldecoder

from _codecs_jp import getcodec, getincrementalencoder, getincrementaldecoder

from _codecs_kr import getcodec, getincrementalencoder, getincrementaldecoder

from _codecs_tw import getcodec, getincrementalencoder, getincrementaldecoder

def __init__(self, *args, **kwargs): # real signature unknown
    pass

def __getitem__(*args, **kwargs): # real signature unknown
    """
    Codec registry lookup.
    
        Returns a CodecInfo object for encoding/decoding and incremental
        encoding/decoding.
    
        Raises a Key
