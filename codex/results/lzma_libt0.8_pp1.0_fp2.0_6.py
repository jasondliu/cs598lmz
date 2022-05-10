import lzma
lzma.open()

#lzma.open(filename, mode='rb', format=None, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

#value=lzma.open(file, mode='rb')

with open("/Users/paulsin/Documents/Python/Python100/100Days/100-days-python-code/Day08/8.txt",'r') as f:
    f_content=f.read()
    f_new=lzma.open("8.txt.xz",'w')
    f_new.write(f_content)
with lzma.open("/Users/paulsin/Documents/Python/Python100/Python100/100Days/100-days-python-code/Day08/8.txt.xz") as f:
    file_content=f.read()
    print(file_content)


'''
zipfile
'''
import zipfile
#zipfile.is_zipfile("8.txt.xz")


#z=
