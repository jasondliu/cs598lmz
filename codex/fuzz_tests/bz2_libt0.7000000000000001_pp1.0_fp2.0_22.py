import bz2
bz2.compress(b'hello world!')

# 我们将得到一个二进制的压缩包，但是它并不是一个标准的gzip或者zip文件，
# 它只包含了bz2模块所能理解的那一部分。
# 假设我们要压缩一个大文件，上面的方法是比较麻烦的，可以使用BZ2File来实现：

with bz2.open('/tmp/example.bz2', 'wt') as f:
    f.write('hello world!')

with bz2.open('/tmp/example.bz2', 'rt') as f:
    print(f.read
