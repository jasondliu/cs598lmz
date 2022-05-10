import mmap, os
from os.path import getsize
from s2protocol import versions, protocol51

class Replay(object):
    def __init__(self, game, protocol):
        self.game = game
        self.protocol = protocol

    def __repr__(self):
        return '<Replay %s %s>' % (self.game, self.protocol)

def read_replay_file(path):
    with open(path, 'rb') as f:
        data = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        decoder = protocol51.Decoder(data)
        header = decoder.read_header()
        # Only support version 1.0.0.51, it shouldn't be too hard to add support for newer versions
        # in the future, but 1.0.0.51 is the oldest supported version.
        if header.m_version.m_baseBuild not in versions:
            raise NotImplementedError('Unsupported replay version %s' % header.m_version.m_
