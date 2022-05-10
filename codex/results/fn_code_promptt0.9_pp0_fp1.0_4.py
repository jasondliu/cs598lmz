fn = lambda: None
# Test fn.__code__
co_name = "test_name"
co_argcount = 10

# SubTest ##############################################
obj = SubTest.SubTest(fn)
assert obj.fn==fn
obj = SubTest.SubTest(fn=fn)
assert obj.fn==fn
assert obj.name ==""
obj = SubTest.SubTest(fn=fn, name=co_name)
assert obj.fn==fn
assert obj.name ==co_name

with SubTest.SubTest(fn=fn, name=co_name, arg_count=co_argcount) as tst:
  pass
del tst # shouldn't raise UnboundLocalError

with SubTest.SubTest(fn, name=co_name, arg_count=co_argcount) as tst:
  pass
del tst # shouldn't raise UnboundLocalError

########################################################
# TestParm #############################################
obj = TestParm.TestParm(fn)
assert obj.fn==fn
obj = TestParm.TestParm(fn=fn)
assert obj.fn==fn
