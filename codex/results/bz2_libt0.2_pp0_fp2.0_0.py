import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 另一个例子是，当我们拷贝文件时，为了保证内容不出错，可以通过反复解压校验来完成：

import bz2
with open('file.txt', 'rb') as f_in, bz2.open('file.txt.bz2', 'wb') as f_out:
    f_out.writelines(f_in)
with open('file.txt', 'rb') as f_in, bz2.open('file.txt.bz2', 'rb') as f_out:
    f_in.seek(0)
    f_out.seek(0)
    while f_in.read(100) == f_out.read(100):
        pass

# 压缩
