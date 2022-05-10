from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
 
# gzip.open
import gzip
with gzip.open('file.txt.gz', 'rb') as f:
    file_content = f.read()
print(file_content)
 
# zipfile.ZipFile
import zipfile
with zipfile.ZipFile('file.zip', 'r') as f:
    for file_name in f.namelist():
        print(file_name)
        file_content = f.read(file_name)
        print(file_content)
        # ...
 
# tarfile.TarFile
import tarfile
with tarfile.open('file.tar.gz', 'r:gz') as f:
    for file_name in f.getnames():
        print(file_name)
        file_content = f.extractfile(file_name).read()
        print(file_content)
        # ...
```
## 6.2 上传文件
```python
    def upload_file(request):
        if request.method == "POST":   
