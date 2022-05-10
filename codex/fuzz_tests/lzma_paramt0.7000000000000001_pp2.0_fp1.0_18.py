from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# 8.3.3 处理不同编码的字符串
# 关于字符编码的问题，Python 提供了一些常用的工具来处理
# 在以下代码中，原始的字符串使用了非标准的编码（latin-1）
s = 'pýtĥöñ\fis\tawesome\r\n'
# 为了在文本模式下将它写入到文件中，要先使用编码将其转换成标准的 Unicode 编码
remap = {
    ord('\t
