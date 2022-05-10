gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.send
print(gi.send(None))
# Test gi.throw
try:
    gi.throw(Exception)
except Exception as e:
    print(e)
# Test gi.close
gi.close()
# Test gi.gi_frame
print(gi.gi_frame)
