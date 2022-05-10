import ctypes
# Test ctypes.CFUNCTYPE( ctypes.POINTER( ctypes.c_int ), ctypes.c_int )
class C_int_p( ctypes.Structure ):
    pass

C_int_p_p = ctypes.POINTER( C_int_p )
C_int_p_p._type_ = C_int_p

C_int_p._fields_ = [ ( "value", ctypes.c_int ) ]

@ctypes.CFUNCTYPE( C_int_p_p, ctypes.c_int )
def test_function( i ):
    #print "Calling test_function with", i
    return C_int_p( i )

class TestStruct( ctypes.Structure ):
    _fields_ = [ ( "callback", ctypes.CFUNCTYPE( C_int_p_p, ctypes.c_int ) ) ]

class TestCallback( object ):
    def __init__( self ):
        self.callback = TestStruct()
        self.callback.callback = test_function

# Test ctypes.CFUNCT
