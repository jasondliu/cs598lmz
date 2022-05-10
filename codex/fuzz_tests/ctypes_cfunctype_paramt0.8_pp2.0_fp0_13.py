import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)
def jit_function(sig, kernel, backend=None, call_helper=None, inline=None):
    """Generate a function implementing the kernel.
    Parameters
    ----------
    sig : str
      The signature of the function to compile
    kernel : str
      The C code to compile
    backend : str, optional
      The compiler backend to use, or None to use the current default
    call_helper : str, optional
      C code to use to call the generated code
    inline : str, optional
      C code to use as a header
    """
    if call_helper is None:
        call_helper = PYFUNCTYPE_CALL
    return jit(sig, kernel, backend=backend, call_helper=call_helper,
               inline=inline, helpervar=PYFUNCTYPE_HELPERVAR)

#------------------------------------------------------------------------
# Testing
#------------------------------------------------------------------------

def test_cuda_compile():
    f = jit_function(args, body, backend='cuda')
