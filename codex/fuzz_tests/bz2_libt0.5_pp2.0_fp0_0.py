import bz2
bz2.decompress(data)

# bz2.BZ2File
# bz2.compress
# bz2.decompress

# 压缩和解压缩gzip文件
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# gzip.open()
# gzip.compress
# gzip.decompress

# 压缩和解压缩zip文件
with zipfile.ZipFile('somefile.zip', 'r') as zf:
    pass

# zipfile.ZipFile
# zipfile.ZipInfo
# zipfile.ZipInfo.filename
# zipfile.ZipInfo.date_time
# zipfile.ZipInfo.compress_size
# zipfile.ZipInfo.file_size
# zipfile.ZipInfo.compress_type
#
