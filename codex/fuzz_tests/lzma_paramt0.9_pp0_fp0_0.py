from lzma import LZMADecompressor
LZMADecompressor().decompress(value)
</code>
If this aspect of what you're doing is finished and tested, then you could consider storing the <code>LZMADecompressor</code> in a global, shared by all future invocations of your page:
<code>from threading import Lock
import lzma

LZMADecompressorCache = {}
LZMADecompressorLock = Lock()

def decompress(value):
    global LZMADecompressorCache, LZMADecompressorLock

    LZMADecompressorLock.acquire(True)
    try:
        return LZMADecompressorCache[id(value)].decompress(value)
    except KeyError:
        result = LZMADecompressorCache[id(value)] = lzma.LZMADecompressor().decompress(value)
        return result
    finally:
        LZMADecompressorLock.release()
</code>

