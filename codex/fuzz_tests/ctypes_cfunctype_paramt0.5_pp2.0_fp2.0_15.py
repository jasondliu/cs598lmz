import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_double,ctypes.c_double,ctypes.c_double,ctypes.c_double)

def set_f(f):
    f_c = FUNTYPE(f)
    lib.set_f(f_c)

def set_df(df):
    df_c = FUNTYPE(df)
    lib.set_df(df_c)

def set_d2f(d2f):
    d2f_c = FUNTYPE(d2f)
    lib.set_d2f(d2f_c)

def set_d3f(d3f):
    d3f_c = FUNTYPE(d3f)
    lib.set_d3f(d3f_c)

def set_d4f(d4f):
    d4f_c = FUNTYPE(d4f)
    lib.set_d4f(d4f_c)

def set_d5f(d5f):
    d5f_c = FUNTYPE(d5f)

