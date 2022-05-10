import codecs
codecs.register_error("strict", codecs.ignore_errors)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--samples", type=int, help="number of samples from corpus")
args = parser.parse_args()

# register 'escapehtml' codec
import re

# a codec to escape HTML
class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        return re.sub(">","&gt;",input,errors=errors), len(input)
    def decode(self,input,errors='strict'):
        return re.sub("&gt;",">",input,errors=errors), len(input)

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

def search_function(encoding):
    if encoding != 'escapehtml':
        return None
    # Assume escapehtml whenever called.
    return codecs.CodecInfo(
        name='escape
