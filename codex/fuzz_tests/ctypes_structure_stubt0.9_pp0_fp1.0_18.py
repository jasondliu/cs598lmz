import ctypes

class S(ctypes.Structure):
    x = 0
    y = 1
    S._pack_ = 1
    S._fields_ = [("x", ctypes.c_long),
                  ("y", ctypes.c_long),
                  ("z", ctypes.c_long)]
s = S()

class S2(ctypes.Structure):
    s = s
    S2._fields_ = [("s", S),
                   ("s2", S)]
s2 = S2()

# Packing was not considered when reordering fields.  Because of this
# a struct without the packed attribute was considered if there was
# a padding field.  Under this scenario the reordering of fields in
# an S2 type would have been unexpected.
#
# Using a packed struct results in the "size" of a field being equal
# to its "offset_or_fortran_descriptor".  This allows ctypes to
# reorder fields to minimize the amount of padding fields.
print "starting offsets:", [f[1] for f in s2._fields_]
print "starting sizes:", [f[2] for f in s
