import io
class File(io.RawIOBase):
    def __init__(self,path='None'):
        self.path = path
    def write(self,b):
        s = b
        if(self.path is not 'None'):
            f = open(self.path,'w')
            f.write(s)
            f.close()
        return len(s)
str1 = "Hello"
str2 = "Hi"
f = File()
f.write(str1+"\n")
f.write(str2)

f.path = 'a.txt'
f.write('\nhi')

print(open('a.txt','r').read())

f.path = 'b.txt'
f.write("hello")
print(open('b.txt','r').read())

class String():
    def __init__(self,b):
        self.b = b
    def __sub__(self,a):
        s = ''
        for i in range(len(self.b)):
            s+=self.b[i].lower() - a[i].lower
