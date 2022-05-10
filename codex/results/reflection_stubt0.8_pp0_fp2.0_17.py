fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
"""
import test_create
run_test(test_create)

import test_print
run_test(test_print)

#import test_math1
#run_test(test_math1)

#import test_math2
#run_test(test_math2)

#import test_localvars
#run_test(test_localvars)

#import test_builtin
#run_test(test_builtin)

#import test_indirect
#run_test(test_indirect)

#import test_func
#run_test(test_func)

#import test_module
#run_test(test_module)

#import test_class
#run_test(test_class)

#import test_method
#run_test(test_method)

#import test_openfile
#run_test(test_openfile)

#import test_filesystem
#run_test(test_filesystem)

#import test_os
#run_test(test_os)


