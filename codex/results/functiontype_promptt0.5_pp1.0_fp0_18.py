import types
# Test types.FunctionType
#
# NOTE: This test is not run automatically, as it requires a working
# Python interpreter to be installed.

import sys, os

def test(cmd):
    print "testing", cmd
    rc = os.system(cmd)
    if rc != 0:
        print "testing", cmd, "failed!"
        print "testing", cmd, "failed!"
        print "testing", cmd, "failed!"
        sys.exit(rc)

test("""%s -c "import types; print types.FunctionType" """ % sys.executable)

test("""%s -c "import types; print types.FunctionType.__doc__" """ % sys.executable)

test("""%s -c "import types; print types.FunctionType.__name__" """ % sys.executable)

test("""%s -c "import types; print types.FunctionType.__module__" """ % sys.executable)

test("""%s -c "import types; print types.FunctionType.func_code" """ % sys.executable)

test("""
