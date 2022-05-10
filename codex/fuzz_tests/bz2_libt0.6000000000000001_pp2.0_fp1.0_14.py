import bz2
bz2_file = bz2.BZ2File('C:\\Users\\Sachin\\Desktop\\file.bz2')
data = bz2_file.read()
bz2_file.close()
print(data)
