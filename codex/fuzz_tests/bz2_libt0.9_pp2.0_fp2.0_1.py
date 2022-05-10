import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
import dis

dis.dis(bz2.BZ2Decompressor.decompress)


class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1"
urllib._urlopener = AppURLopener()
urllib._urlopener.retrieve(
    'http://www.pythonchallenge.com/pc/ring/guido.html', 'file/guido.html')


#
