from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = '&lt;3s3sHH'
s.size = calcsize(s.format)
</code>

