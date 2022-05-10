import _struct
w=_struct.pack("i",2002)
print(len(w))

var1=11
var2=12
w=str(var1)+str(var2)
print(w)
print(int(w))

f=open("/home/administrator/Gemfield/py/a.txt","rb")
print(f.read(1024))
#f.read(1024)
print(f.tell())
f.seek(0)
print(f.read(1024))
print(f.tell())
f.close()

f=open("/home/administrator/Gemfield/py/b.txt","w")
f.writelines("This is a test.\nreally?\n")
