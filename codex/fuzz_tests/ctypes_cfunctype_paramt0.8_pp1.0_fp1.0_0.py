import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int)

def enable_python_hooks(enable):
    import sys
    def call(event_name, data):
        if event_name == 'malloc':
            sys.stdout.write('Calling %s (%d)... ' % (event_name, data))
            sys.stdout.write('Done\n')
        else:
            sys.stdout.write('Calling %s\n' % (event_name,))
        return 0
    if enable:
        print "Enabling hooks (python)"
        ljd.rawseti(addr, -11, FUNTYPE(call)())
    else:
        print "Disabling hooks (python)"
        ljd.rawseti(addr, -11, 0)

enable_python_hooks(True)
