gi = (i for i in ())
# Test gi.gi_code.co_name
print(next(gi).__name__)
# Test gi.gi_frame
print(next(gi).f_code.co_name)
gi.gi_frame = None
print(next(gi).f_code.co_name)
# Test gi.gi_running
record = []
def check_state(state):
    record.append(gi.gi_running)
    record.append(state)
gi.gi_running = False
check_state(None)
gi.gi_running = True
check_state(True)
gi.gi_running = False
check_state(False)
print(record)

# Check range_obj
print(range_obj.__reduce__())
print(range_obj.__reduce_ex__(2))

# Check MemoryIO
s = BytesIO(b"spam")
r = loads(dumps(s))
print(r.getvalue())

# Check back references
l = [1, 2, 3]
l.append(l)
l2 = loads(dumps
