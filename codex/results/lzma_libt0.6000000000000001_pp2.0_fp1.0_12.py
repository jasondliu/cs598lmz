import lzma
lzma.open(path)

# 使用参数指定打开文件的模式
lzma.open(path, mode='r')
lzma.open(path, mode='rb')
lzma.open(path, mode='rt')

# 如果文件已经被打开，可以直接使用文件句柄
lzma.open(f)
lzma.open(f, mode='r')
lzma.open(f, mode='rb')
lzma.open(f, mode='rt')
```

## 读取数据

从文件中读取数据，使用 `read` 方法。

```python
# 读取所有数据
lzma.open(path).read()


