import codecs
# Test codecs.register_error!

# Based on a post by Michael Urman in comp.lang.python

import codecs
import os, urllib

_debug = 0

CODEC_LATIN1 = 'latin1'
CODEC_UTF8   = 'utf-8'

def debug(msg):
    if _debug:
        print(msg)

class MyErrorHandler:
    def __init__(self, codec_undecodable, codec_replace):
        self.codec_undecodable = codec_undecodable
        self.codec_replace = codec_replace
        self.errors = []
        self.replacements = []
        self.state = u""

    def handle(self, exc):
        if isinstance(exc, UnicodeEncodeError):
            self.errors.append((self.state, exc.object[exc.start:exc.end]))
            self.replacements.append((self.state, u"*%s*" % exc.object[exc.start:exc.end].encode(self.codec_replace)))
