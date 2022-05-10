import _struct
# Test _struct.Struct
def test_Constructor_Parameterized():
    """_struct.Struct(format[, name])"""
    Struc = _struct.Struct
    s = Struc('i')
    assert repr(s) == "Struct('i')"
    s = Struc('b','nameHere')
    assert repr(s) == "Struct('b','nameHere')"
    #
    s = Struc()
    try: s = Struc('')
    except ValueError: pass
    else: print "Expected error for %r" % s
    try: s = Struc('X')
    except ValueError: pass
    else: print "Expected error for %r" % s
    try: s = Struc('9')
    except ValueError: pass
    else: print "Expected error for %r" % s
    try: s = Struc('-')
    except ValueError: pass
    else: print "Expected error for %r" % s
    try: s = Struc('I','')
    except ValueError: pass
    else: print "Expected error
