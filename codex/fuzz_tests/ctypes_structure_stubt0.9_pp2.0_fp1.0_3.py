import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_int16()
    z = ctypes.c_int16()
    w = ctypes.c_int16()

obj = S()
obj.x = 1
obj.y = 2
obj.w = 0
print(obj.z is None)
</code>
Is outputing <code>True</code>. Could you please tell me why?


A:

Thanks to @eryksun. As for <code>S</code> being class attribute, it does not look like <code>obj</code> is a unique object, so it could inherit <code>z</code> attribute from other <code>x</code> objects. 
<code>obj.z = None</code> gets assigned and <code>obj.z is None</code> evaluates false.

