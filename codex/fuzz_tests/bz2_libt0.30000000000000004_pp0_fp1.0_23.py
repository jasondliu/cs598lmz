import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 压缩文件
with open('test.txt', 'rb') as f_in, bz2.BZ2File('test.txt.bz2', 'wb') as f_out:
    f_out.writelines(f_in)

# 解压文件
with bz2.BZ2File('test.txt.bz2', 'rb') as f_in, open('test.txt', 'wb') as f_out:
    f_out.writelines(f_in)

# 压缩和解压文件的简单方法
import bz2
with bz2.open('test.txt.bz2', 'wt') as f_out:
    f_out.write('hello world!')

with bz2.open('test.txt.bz2', 'rt') as f_in:
    text = f_in.read()
