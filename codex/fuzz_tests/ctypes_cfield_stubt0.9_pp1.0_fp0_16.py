import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

cursor = self.make_cursor()

cursor.visit_field(S.x)
cursor.visit_field(S.x, "foo")

cursor = self.make_cursor()

cursor.visit_field(S.x)
cursor.visit_field(S.x.name)
cursor.visit_field(S.x.name, "foo")

cursor = self.make_cursor("c_int")

cursor.visit_field(S.x)
cursor.visit_field("S.x")
cursor.visit_field("S.x", "foo")
