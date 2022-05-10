import weakref
# Test weakref.ref(A()) == weakref.ref(A())
# From: http://bugs.python.org/issue2636
#
# Returns the [return value, exception details] or [exception details]
#

def runner(func, *args):
    try:
        return [func(*args), None]
    except Exception as e:
        return [None, e]


def check(arg):
    from _testcapi import getargs_keywords_only
    return getargs_keywords_only(arg)


#
# make sure the builtin types can be used as the keyword_only parameter
#

def test_single_type():
    for type in sorted(set(sys.builtin_module_names) & set(sys.modules)):
        m = sys.modules[type]
        # don't test modules that don't define any type
        if not hasattr(m, '__all__'):
            continue

        # skip these modules, as they will not work correctly with keyword-only
        if type in ['re', '__main__']:
            continue

       
