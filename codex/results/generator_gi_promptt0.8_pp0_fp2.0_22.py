gi = (i for i in ())
# Test gi.gi_code
gi = (i for i in ())
try:
    test_support.run_doctest(sys.gen_profile.functions[gi.gi_code].co_linecache, verbose)
    test_support.run_doctest(sys.gen_profile.functions[gi.gi_code].co_linecache.__class__, verbose)
    test_support.run_doctest(sys.gen_profile.functions[gi.gi_code].co_linecache.lines.__class__, verbose)
    test_support.run_doctest(sys.gen_profile.functions[gi.gi_code].co_linecache.lines, verbose)
except AttributeError:
    # On PyPy, 'sys.gen_profile' is missing.
    pass

# Test sys.flags
test_support.run_doctest(sys.flags, verbose)

# Test sys._debugmallocstats
test_support.run_doctest(sys._debugmallocstats, verbose)

# Test sys.setswitchinter
