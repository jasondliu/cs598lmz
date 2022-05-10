import types
# Test types.FunctionType and types.LambdaType types, as
# well as creation of function objects.

def global_test(): pass
g = global_test

f_inner, f_outer = type(g), type(global_test)

def func_type_test(f):
    if type(f) is not f_inner:
        print("global_test type fail")

def lambda_type_test(x):
    f = lambda: x
    f_type = type(f)
    try:
        if f_type is not f_outer:
            print("Lambda function type fail")
    except:
        print("Identity comparison of Lambda type fail")
    if isinstance(f, types.FunctionType):
        print("isinstance of Lambda function OK")
    else:
        print("isinstance of Lambda function fail")


PRIM_TYPES = (
    None, True, False,
    1, 2L, 1.0, 1.0+0j,
    "abc", u"uabc", buffer("buff"),
    (1,
