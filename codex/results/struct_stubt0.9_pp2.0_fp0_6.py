from _struct import Struct
s = Struct.__new__(Struct)
s.format = '9s'

mystring1 = "Apple"
mystring2 = "Pencil"
mystring3 = "Cookie"
mystring4 = "Balloon"
mystring5 = "Chipmunk"
mystring_list = mystring1+mystring2+mystring3+mystring4+mystring5
s.unpack(mystring_list)
mystring_list
</code>
Output:
<code>'ApplePencilCookieBalloonChipmunk'
</code>


A:

You need to loop over the string list to pass the raw string while unpacking.It will unpack the bytes into the tuple.    
<code>from _struct import Struct
s = Struct.__new__(Struct)
s.format = '9s'

mystring1 = "Apple"
mystring2 = "Pencil"
mystring3 = "Cookie"
mystring4 = "Balloon"
mystring5 = "Chipmunk"
mystring_list = mystring1+mystring2+mystring3+mystring4+my
