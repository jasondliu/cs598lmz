import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

print("Generating the random functions")
#random.seed(0)

functs = [random_function(random.randrange(1,4)) for _ in range(0,5)]

for f in functs:
    print("generated function:")
    print("\t",f)

print("evaluating the functions")

for f in functs:
    print("function:",f)
    f = FUNTYPE(f)
    print("\t",f(1.23))

print("finished!")
