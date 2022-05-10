import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double
    
def main():
    obj = S()
    
    obj.x = 1.0
    obj.y = 2.0
    obj.z = 3.5
    
    return obj
    
if __name__ == '__main__':
    obj = main()
    print(obj)
