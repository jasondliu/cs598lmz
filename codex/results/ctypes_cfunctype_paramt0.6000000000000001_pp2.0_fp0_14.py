import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def cos_func(x):
    return math.cos(x)

cos_func_ptr = FUNTYPE(cos_func)

def main():

    x = 0.0
    while x < 1.0:
        print("cos_func({0}) = {1}".format(x, cos_func(x)))
        x += 0.1

    print("\n")

    x = 0.0
    while x < 1.0:
        print("cos_func_ptr({0}) = {1}".format(x, cos_func_ptr(x)))
        x += 0.1

if __name__ == "__main__":
    main()
