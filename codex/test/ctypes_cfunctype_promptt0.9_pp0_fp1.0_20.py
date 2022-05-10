import ctypes
# Test ctypes.CFUNCTYPE() is working on WIN64 Python 2.u
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(i, j): 
    """
    >>> func
    <CFUNCTYPE(c_int, c_int) object at 0x0287CD20>
    """
    ...

def func4(i):
    """
    >>> func4
    <CFUNCTYPE(c_int, c_int) object at 0x0287CD88>
    """

    return func(i, 4)

class Spam:
    @ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    def meth(self, i, j): 
        """
        >>> Spam.meth
        <ctypes.CFUNCTYPE object at 0x026EEE80>

        >>> Spam.meth is Spam.meth
        True
        """
        ...

