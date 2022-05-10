gi = (i for i in ())
# Test gi.gi_code.co_varnames (= ('i',)) before the next line
gi.send(None)
result = gen.send((42, 100))
print result
print type(result)
print result[0]
print result[1]
