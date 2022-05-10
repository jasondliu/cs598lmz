import lzma
lzma.decompress(LZMA_READ(input_file))

```

```
import os
os.mkdir(dir=str)
os.chdir(dir=str)

```

```
with open('s1.py', 'rb') as f:
    print(f.read())
    print(f.read())#Nothing

```

```
open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)#就是python的打开文件的方法
mode:
    'r':只读
    'w':只写
    'a':追加
    'r+':读写
    'b':二进制
    't':文本

```



```
os.listdir('/')#os.listdir(path='./')

```

###
