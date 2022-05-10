import bz2
# Test BZ2Decompressor

with bz2.open(r'C:\Users\user\Desktop\week1\test.txt.bz2',mode='wt') as file:
    file.write('a'*100)
with bz2.open(r'C:\Users\user\Desktop\week1\test.txt.bz2', mode='rb') as file:
    print(file.read())

with bz2.BZ2File(r'C:\Users\user\Desktop\week1\test.txt.bz2', mode='wb') as file:
    file.write(b'a'*100)
with bz2.BZ2File(r'C:\Users\user\Desktop\week1\test.txt.bz2', mode='rb') as file:
    print(file.read())

with open(r'C:\Users\user\Desktop\week1\test.txt',mode='wb') as file:
    file.write(b'd'*100)
