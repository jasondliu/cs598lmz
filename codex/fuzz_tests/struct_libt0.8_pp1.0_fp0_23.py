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
    __map_cp932ext = mbc.__map_build(
        mbc.__map_cp932ext,
        u"\u3000\u30fc\u309c\u309d\u309e\uff61\uff67\uff68\uff69\uff6a"
        u"\uff6b\uff6c\uff6d\uff6e\uff6f\uff70\uff71\uff72\uff73\uff74"

