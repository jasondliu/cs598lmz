from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 这个类也支持一个基于块的接口，可以用来压缩或解压数据流。
# 下面是一个压缩数据的例子：
import lzma
compressor = lzma.LZMACompressor()
with open('lorem.xz', 'wb') as f:
    f.write(compressor.compress(b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam metus velit, dictum id sapien non, congue varius turpis. Fusce at tincidunt leo. Quisque dapibus, sapien id commodo volutpat, dolor erat volutpat nisl, nec ultrices nisl nunc vitae nisi. Nulla facilisi. Nulla facilisi.
