import ctypes

class S(ctypes.Structure):
    x = 123

print('before S.x=321'+str(S.x))
S.x = 321    
print('after S.x=321'+str(S.x))
