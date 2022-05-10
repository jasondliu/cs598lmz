gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.send()
gi.send(1)
# Test gi.throw()
gi.throw(Exception())
# Test gi.close()
gi.close()

# Test inspect.isgenerator()
inspect.isgenerator(gi)

# Test inspect.getgeneratorlocals()
inspect.getgeneratorlocals(gi)

# Test inspect.getgeneratorstate()
inspect.getgeneratorstate(gi)

# Test inspect.getgeneratorframe()
inspect.getgeneratorframe(gi)

# Test gi.gi_frame.f_lasti
gi.gi_frame.f_lasti
# Test gi.gi_frame.f_lineno
gi.gi_frame.f_lin
