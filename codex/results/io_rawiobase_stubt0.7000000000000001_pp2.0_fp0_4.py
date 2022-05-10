import io
class File(io.RawIOBase):
    def read(self,n=-1):
        return super().read(n)
    def readline(self,limit=-1):
        return super().readline(limit)
    def seek(self,offset,whence=0):
        super().seek(offset,whence)
    def tell(self):
        return super().tell()
    def write(self,b):
        super().write(b)

'''
文件对象接口
'''
File.write(b"haha")

#内存文件
# mmap.mmap(fileno,length,tagname=None,access=mmap.ACCESS_WRITE)

#编码
# import codecs
# with codecs.open(file,mode,encoding=None,errors=None,buffering=None)

#压缩文件
# import gzip
# with gzip.open(filename,"wt") as f:
#     f.write("hello gzip")

''
