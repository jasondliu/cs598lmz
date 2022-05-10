from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

### 使用zipfile模块解压

```python
import zipfile
zipfile.ZipFile(filename,mode='r',compression=zipfile.ZIP_LZMA).extractall(path)
```

### 使用shutil模块解压

```python
import shutil
shutil.unpack_archive(filename,extract_dir=None,format='zip')
```

### 纯命令行操作

```shell
# 只支持zip格式的解压
unzip xxx.zip

# 只支持xz格式的解压
tar xvf xxx.xz
```



## 命令行操作解压

### tar操作

### 参数说明

