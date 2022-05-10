import ctypes
ctypes.c_void_p()
</code>
Where does this pointer go ?


A:

It gets set to <code>nullptr</code>. <code>c_void_p</code> has no implicit conversion from <code>None</code> so the latter side is considered to be error, which is an acceptable value for <code>nullptr</code>.

