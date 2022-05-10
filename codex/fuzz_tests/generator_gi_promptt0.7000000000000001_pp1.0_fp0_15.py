gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_trace
def foo():
    print("Foo")
    return foo
gi.gi_frame.f_trace = foo
print(gi.gi_frame.f_trace())

print('\n### Test sys.argv')
print(sys.argv)

print('\n### Test sys.version')
print(sys.version)

print('\n### Test sys.version_info')
print(sys.version_info)

print('\n### Test sys.platform')
print(sys.platform)

print('\n### Test sys.path')
print(sys.path)

print('\n### Test sys.path_hooks')
print(sys.path_hooks)

print('\n### Test sys.path_importer_cache')
print(sys.path_importer_cache)


