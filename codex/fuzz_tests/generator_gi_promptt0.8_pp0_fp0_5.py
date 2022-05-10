gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code is None
# Test gi.gi_frame
assert gi.gi_frame is None
# Test gi.gi_running
assert gi.gi_running is False
# Test gi.gi_name
assert gi.gi_name == "i"
# Test gi.gi_yieldfrom
raise TestError("gi.gi_yieldfrom not defined")

gi = (i for i in (j for j in ()))
# Test nested gi.gi_yieldfrom
raise TestError("gi.gi_yieldfrom not defined")

# Test gi.close()
raise TestError("gi.close() does not work")
# Test gi.throw()
raise TestError("gi.throw() does not work")
# Test gi.send()
raise TestError("gi.send() does not work")
