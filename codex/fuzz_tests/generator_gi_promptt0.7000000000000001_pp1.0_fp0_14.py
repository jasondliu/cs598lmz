gi = (i for i in ())
# Test gi.gi_code
test_gi.gi_code.co_code
test_gi.gi_code.co_flags
test_gi.gi_frame
test_gi.gi_frame.f_code.co_code
test_gi.gi_frame.f_code.co_flags
test_gi.gi_frame.f_code.co_name

# Test array.array
test_array = array.array("H", [1,2,3])
test_array[0]
test_array[2]
test_array.append(4)
test_array.count(1)
test_array.extend([5,6])
test_array.fromfile(io.BytesIO(b"\x00\x01\x02\x03\x04\x05\x06\x07"), 4)
test_array.fromlist([1,2,3])
test_array.fromstring(b"\x00\x01\x02\x03")
test_array.index(3, 1)
test_array.insert(1, 0)
test_array.
