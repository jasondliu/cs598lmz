import lzma
# Test LZMADecompressor
# d = lzma.LZMADecompressor()
# data = d.decompress('...')
# print(data)

#  解压缩
def decompress(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
        d = lzma.LZMADecompressor()
        data = d.decompress(file_content)
    return data

# # 打包
# 使用make_archive()函数创建ZIP文件，使用register_extractor()注册和解压的类：

# from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
#
# def make_zip(source_dir, output_filename):
#     relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
#     with ZipFile(output_filename, "w", ZIP_DEFL
