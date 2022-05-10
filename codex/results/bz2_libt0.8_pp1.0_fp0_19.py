import bz2
bz2.BZ2File(f1.name).read()

# 生成文件对象并写入数据
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

# 读取文件前2个字节
with open('somefile.bin', 'rb') as f:
    data = f.read(2)
    print(data)

# 文件的二进制形式
with open('somefile.bin', 'rb') as f:
    data = f.read(8)
    print(data)
    text = data.decode('utf8')
    print(text)

# 文件的字符串解码
with open('somefile.bin', 'rb') as f:
    data = f.read(8)
    print(data)
    text = data.decode('utf8')
   
