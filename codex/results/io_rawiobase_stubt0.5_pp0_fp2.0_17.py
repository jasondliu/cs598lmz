import io
class File(io.RawIOBase):
    def read(self,n=-1):
        return b'\x00'*n
    def write(self,b):
        pass
    def tell(self):
        return 0
    def seek(self,offset,whence=0):
        pass
    def close(self):
        pass

f = File()
f.write(b'hello')
print(f.read(10))
f.seek(5)
f.close()

# 文件对象
# 在Python中，文件对象就是一个类似于上面的File类的实例。
# 它有一个名为fileno()的方法，返回一个整数，表示与该文件相关联的底层文件描述符（file descriptor）。

#
