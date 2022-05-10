import _struct
import _unicodedata
import _codecs_cn
import _codecs_hk
import _codecs_iso2022
import _codecs_jp
import _codecs_kr
import _codecs_tw
import encodings
import _osx_support

def getregentry():
    return encodings.codec_map_mac['mac-japanese']

__map_cp932ext = None

def __map_cp932ext_init():
    import _multibytecodec as mbc
    global __map_cp932ext
