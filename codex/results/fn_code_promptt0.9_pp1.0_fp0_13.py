fn = lambda: None
# Test fn.__code__.co_varnames
checkAll(
     name="__code__.co_varnames",
     ref=["x", "y"],
     fn=lambda x, y: None)
# Test fn.__defaults__
checkAll(
     name="__defaults__",
     ref=[1],
     fn=lambda x, y=1: None)
# Test fn.__kwdefaults__
checkAll(
     name="__kwdefaults__",
     ref={"y": 1},
     fn=lambda x, y=1: None)
# Test fn.__annotations__
checkAll(
     name="__annotations__",
     ref={"x": 1, "y": True},
     fn=lambda x: None,
     annotations={"x": 1, "y": True})
# Test fn.__call__
# checkAll(prints="""<function outer.__call__()>""",
#           fn=emptyFn)
# Test fn.__closure__
# Test fn.__closure_values__
checkAll(
     name="__closure
