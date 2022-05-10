from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__["_fmt"] = ">L"
s.__dict__["format"]

f = Foo()
f.__dict__["_fmt"] = ">L"
f.__dict__["format"]
