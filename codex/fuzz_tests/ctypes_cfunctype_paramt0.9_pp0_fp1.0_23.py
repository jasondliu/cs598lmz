import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

IDENTIFIERS = {
1: ("x", FUNTYPE(lambda: random.randint(1,5))),
2: ("x", FUNTYPE(lambda: random.randint(1,5))),
3: ("x^2", FUNTYPE(lambda: random.randint(1,5))),
4: ("x^2", FUNTYPE(lambda: random.randint(1,5))),
5: ("x^3", FUNTYPE(lambda: random.randint(1,5))),
6: ("x^3", FUNTYPE(lambda: random.randint(1,5))),
7: ("√(x)", FUNTYPE(lambda: random.randint(1,5))),
8: ("√(x)", FUNTYPE(lambda: random.randint(1,5))),
9: ("x!", FUNTYPE(lambda: random.randint(1,5))),
10: ("x!", FUNTYPE(lambda: random.randint(1,5))),
11: ("ln(x)", FUNTYPE(lambda: random.rand
