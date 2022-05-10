import bz2
bz2_comp = bz2.BZ2Compressor()
print(bz2_comp.compress(b'hello world'))
print(bz2_comp.flush())

from io import StringIO
from io import BytesIO
# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 操作文件
