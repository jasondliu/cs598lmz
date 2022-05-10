import _struct

def perf_counter_ns():
    return int(time.perf_counter() * 1e9)

# Convert a c-struct to a python dictionary
def cstruct_to_dict(struct):
    ret = {}
    for field in struct._fields_:
        ret[field[0]] = getattr(struct, field[0])
    return ret

# Convert from native endian to the endian the pot race library expects
if sys.byteorder == "little":
    to_le = lambda x: x
    from_le = lambda x: x
else:
    to_le = lambda x: x.byteswap()
    from_le = lambda x: x.byteswap()

def potrace_trace(input_data, polarity, alphamax, opttolerance):
    c_input_data = ffi.new("double[]", list(input_data))
    c_params = ffi.new("potrace_param_t*", {
        "turnpolicy": lib.POTRACE_TURNPOLICY_MINORITY
