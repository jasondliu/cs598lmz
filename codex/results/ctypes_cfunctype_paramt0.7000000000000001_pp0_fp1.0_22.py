import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def solve_equations(coefs, values):
    # print("solve_equations")
    # print(values)
    # print(coefs)
    n = values.shape[0]
    c = np.zeros(n)
    c[0] = coefs[0] + coefs[1] + coefs[2]
    c[n-1] = coefs[1] + coefs[2]

    for i in range(1, n - 1):
        c[i] = coefs[0] + 2 * coefs[1] + coefs[2]

    b = np.zeros(n)
    b[0] = values[0] * (coefs[0] + 2 * coefs[1] + 2 * coefs[2]) + values[1] * coefs[2] + values[2] * coefs[1]
    b[n-1] = values[n-1] *
