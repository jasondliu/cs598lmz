import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 10

s = S()
s.x[0] = 'A'
s.x[1] = 'B'
s.x[2] = 'C'
print("s.x :",s.x)

print("s.x[0] :",s.x[0])
print("s.x[1] :",s.x[1])
print("s.x[2] :",s.x[2])
print("s.x[3] :",s.x[3])
print("s.x[4] :",s.x[4])
print("s.x[5] :",s.x[5])
print("s.x[6] :",s.x[6])
print("s.x[7] :",s.x[7])
print("s.x[8] :",s.x[8])
print("s.x[9] :",s.x[9])
