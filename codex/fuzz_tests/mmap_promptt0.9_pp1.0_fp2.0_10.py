import mmap
# Test mmap.mmap 
''' 
fd = os.open("taobao",os.O_RDWR, 0777)
buf = mmap.mmap(fd, 0)
print buf
buf[10]='c'
'''
#Test mmap.mmap(length=10)
'''
buf = mmap.mmap(-1, 10)
print buf
buf[9]='a'
'''

# Test write
'''
buf = mmap.mmap(-1, 100)
print buf
print type(buf)
buf.write("\n".join(["adcde", "bcdef","redhat","packt"]))
print buf
buf.seek(0)
print buf[:]
buf.seek(0)
print buf.read(5)
'''

#print buf.find("packt")

# Test flush, rfind in one file
'''
buf = mmap.mmap(-1, 100)
print buf
buf.write("\n".join(["aaadcde", "bbbdef","cccredhat","dddpack
