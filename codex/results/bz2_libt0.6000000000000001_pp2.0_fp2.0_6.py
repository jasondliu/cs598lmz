import bz2
bz2_file = bz2.BZ2File('output.bz2', 'wb')
bz2_file.write(b'hello world')
bz2_file.close()
# 读取文件
bz2_file = bz2.BZ2File('output.bz2', 'rb')
print(bz2_file.read())
bz2_file.close()

# 3. 压缩和解压缩
# bz2.compress(data)
# bz2.decompress(data)

# 4. 压缩和解压缩大文件
# 压缩
import bz2
infile = open('lorem.txt', 'rb')
outfile = bz2.BZ2File('lorem.bz2', 'wb')

for data in iter(lambda: infile.read(100 * 1024), b''):
    outfile.write(data)

outfile.close
