import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123
print(fun()) # -&gt; 123
# access the memory address of the funtion (show rawpointer)
print(ctypes.addressof(fun))
# access the content of the function (show tcode)
print(fun.__code__.co_code)
</code>
I think what you want is:
<code>tcode = fun.__code__.co_code

tmp = []
tmp.append(tcode[0:1])
tmp.append(tcode[1:2])
tmp.append(tcode[2:3])
tmp.append(tcode[3:4])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5])
tmp.append(tcode[4:5
