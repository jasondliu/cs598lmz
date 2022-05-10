import bz2
bz2.decompress(data)

# 使用bz2模块压缩数据
import bz2
data = b'This is the original text.'
bz2.compress(data)

# 使用bz2模块压缩文件
import bz2, sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'rb') as in_file, bz2.BZ2File(output_file, 'wb') as out_file:
    out_file.writelines(in_file)

# 使用bz2模块解压文件
import bz2, sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with bz2.BZ2File(input_file, 'rb') as in_file, open(output_file, 'wb') as out
