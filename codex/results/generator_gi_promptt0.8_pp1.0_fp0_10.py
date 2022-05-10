gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.__next__
print(gi.__next__())
# Test gi.send
print(gi.send(1))
# Test gi.throw
try:
    gi.throw(TypeError)
except TypeError:
    print('TypeError')
# Test gi.close
gi.close()
try:
    gi.__next__()
    print('TypeError not raised')
except TypeError:
    print('TypeError')
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)

# Test __length_hint__
print(len(range(1, 3)))

# Test some methods
i = iter(range(1, 3))
# Test __iter__
i = i.__iter__()
# Test __next__
print(i
