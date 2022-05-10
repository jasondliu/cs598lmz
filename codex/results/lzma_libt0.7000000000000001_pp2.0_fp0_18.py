import lzma
lzma.open('foo.xz').read()
```

Для чтения файлов tar.xz, можно использовать библиотеку tarfile:

```python
import tarfile
import lzma
with tarfile.open('foo.tar.xz', mode='r|xz') as f:
    f.getmembers()
    f.extractall('/my/path')
```

Когда вы имеете дело с достаточно большими файлами, вы можете читать из объекта
lzma.LZMAFile или tarfile.xzfile по бл
