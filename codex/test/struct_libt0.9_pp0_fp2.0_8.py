import _struct
from StringIO import StringIO
import string

from heroprotocol.sc2parser import Decoder

from heroprotocol.protocol import versions
from heroprotocol.protocol.decoders import DECODERS
from heroprotocol.protocol.msgs import MESSAGES, MESSAGE_ID_TO_NAME

from heroprotocol.process import cache

if not cache.initialized():
    cache.init_cache(cache.CACHEDIR)


class TooManyMatches(Exception):

    def __init__(self):
        Exception.__init__(self, "Too many replay matches")


class Replay(object):

    def __init__(self, baseBuild, bytes, *args):
        self.decoder = Decoder(baseBuild)
        self.data = self.decoder.decompress_replay(bytes, *args)
        self.stream = StringIO(self.data)
        self.header_data = self.decoder.decode_replay_header(
            self.data, *args)
