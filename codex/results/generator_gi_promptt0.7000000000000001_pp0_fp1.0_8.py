gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
print("line: {:d}".format(gi.gi_code.co_firstlineno))

# Test gi.gi_frame.f_lineno
print("line: {:d}".format(gi.gi_frame.f_lineno))


# Test gi.gi_frame.f_lasti
print("bytecode offset: {:d}".format(gi.gi_frame.f_lasti))


# Test gi.gi_frame.f_trace
def traceit(fr, event, arg):
    '''
    callback used by sys.settrace()
    '''
    print("traceit:", event, fr.f_lineno, fr.f_code.co_name, fr.f_globals,
          fr.f_locals, arg, sep=' ')
    return traceit

sys.settrace(traceit)
g = (x for x in range(3))
print("line: {:d}".format(g.gi_frame.f_lineno))

for i in g:

