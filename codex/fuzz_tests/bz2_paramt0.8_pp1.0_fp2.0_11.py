from bz2 import BZ2Decompressor
BZ2Decompressor().decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084").decode("utf-8")

import json
def get_jsonparsed_data(url):
    """Receive the content of ``url``, parse it as JSON and return the object.
    url can be compressed with gzip, bzip2 or bz2.
    """
    try:
        if url.endswith(".bz2"):
            import bz2
            response = bz2.decompress(urlopen(url).read())
        elif url.endswith(".gz"):
            import gzip
            response = gzip.decompress(urlopen(url).read())
        else:
            response = urlopen(url).read().decode("utf-8")
        return
