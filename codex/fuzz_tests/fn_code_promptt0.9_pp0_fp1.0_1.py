fn = lambda: None
# Test fn.__code__.co_varnames
#
# @check50.check(compile_test)
# def co_varnames():
#     """lambda() has correct __code__.co_varnames"""
#     check50.exists("test1.py")
#     check50.run("python3 test1.py").stdout("<tuple object>").exit()

# Test fn.__closure__
#
# @check50.check(compile_test)
# def closure():
#     """lambda() has non-None __closure__"""
#     check50.exists("test1.py")
#     check50.run("python3 test1.py").stdout("<tuple object>").exit()

# Test fn.__code__.co_namelist
#
# @check50.check(compile_test)
# def co_namelist():
#     """lambda() has correct __code__.co_namelist"""
#     check50.exists("test1.py")
#     check50.run("python3 test1.py").std
