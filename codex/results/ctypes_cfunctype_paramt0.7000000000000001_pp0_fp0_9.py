import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x*x+1

def fprime(x):
    return 2*x

# Allocate the f and fprime functions as C functions
f_c = FUNTYPE(f)
fprime_c = FUNTYPE(fprime)

# Create the rootfinder
solver = Newton(f_c, fprime_c)

# Set initial value
x0 = 1.

# Solve
solution = solver.solve(x0)

print solution

# Create the rootfinder
solver = Secant(f_c)

# Set initial value
x0 = 1.

# Solve
solution = solver.solve(x0)

print solution

# Create the rootfinder
solver = Halley(f_c, fprime_c)

# Set initial value
x0 = 1.

# Solve
solution = solver.solve(x0)

print solution
