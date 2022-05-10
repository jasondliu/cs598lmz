import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename)

import lzma
lzma.LZMAFile(filename)

import zipfile
zipfile.ZipFile(filename)
```

## 文件夹和目录操作

### 文件夹操作

```python
import os

# 获取当前文件夹
os.getcwd()

# 创建文件夹
os.mkdir(path)

# 删除文件夹
os.rmdir(path)

# 更改文件夹
os.chdir(path)

# 文件夹列表
os.listdir(path)

# 创建多级目录
os.makedirs(path)

# 删除多
