from _struct import Struct
s = Struct.__new__(Struct)
s. format = '&lt;BH'
s.size = s.calcsize(s.format) # 5
</code>
To get the <code>size</code>, simply call the <code>calcsize</code> method on it. 

