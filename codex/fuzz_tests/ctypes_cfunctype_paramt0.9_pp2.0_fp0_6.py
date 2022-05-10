import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, lltype.Signed, lltype.Signed )

fun_cptr = FUNTYPE(func)
fun_rtyper = translate(func)

def call(n):
    res = fun_rtyper.call(n, n)
    return res

def test():
    n = sys.getrecursionlimit() / 2
    x = -123
    eq_( fun_rtyper.call(x, 0), x )
    eq_( fun_rtyper.call(0, x), x )
    res = fun_rtyper.call(n, n)
    res2 = call(n)
    ok_( res >= 0 )
    ok_( res2 >= 0 )

    # test that we can still call the same function with the CPython driver
    for i in range(n):
        p = rffi.cast( rffi.ULONG, fun_cptr )
        eq_( c_function( p, i, i ), i*2+1 )

    if res < n and res2 < n:
        skip("
