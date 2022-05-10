from lzma import LZMADecompressor
LZMADecompressor()
</code>
ну а дальше совсем просто декодируем строку с помощью <code>base64</code>:
<code>from base64 import standard_b64decode
decompressed = lzma_decompressor.decompress(standard_b64decode(data))
</code>

