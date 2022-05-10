gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send(1)
print(gi.send(1))
# Test gi.throw(RuntimeError)
print(gi.throw(RuntimeError))
# Test gi.close()
print(gi.close())
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send(1)
print(gi.send(1))
# Test gi.throw(RuntimeError)
print(gi.throw(RuntimeError))
# Test gi.close()
print(gi.close())

print("=" * 20)

def gen():
    for i in range(
