gi = (i for i in ())
# Test gi.gi_code is <code object <genexpr> at 0x00029530, file "python", line 1>
print 'gi.gi_code', gi.gi_code
#  'gi.gi_code <code object <genexpr> at 0x00029530, file "python", line 1>'
print

# Test PythonScope_New was called with the code object.
# The last line of Python-Scope.py is (must be) the only call to PythonScope_New
# so this must be the PythonScope that was created.
print 'PythonScope_New:', PythonScope_New.func_globals['code']
assert id(PythonScope_New.func_globals['code']) == id(gi.gi_code)
print

print 'PythonScope_Dispose:', PythonScope_Dispose
# PythonScope_Dispose is only called from PythonScope_Dispose in Python-Scope.py
# so we find the PythonScope at PythonScope_Dispose.func_globals['PythonScope_Dispose']
assert 'PythonScope_Dispose' in PythonScope_Dispose.func
