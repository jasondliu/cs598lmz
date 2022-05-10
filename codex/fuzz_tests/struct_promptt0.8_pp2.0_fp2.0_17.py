import _struct
# Test _struct.Struct.format_map()
# See Issue #15771

FORMAT_MAP_TESTS = [
    ("ii", [], {}),
    ("iiP", [], {}),
    ("iiP", [4, 2, 15], {"P": 10}),
    ("Pii", [4, 2, 15], {"P": 10}),
    ("Pii", [4, 2, 15], {"P": "abc"}),
    ("iP", [], {"P": 10}),
    ("ii", [], {"P": 10}),
    ("iP", [10], {"P": 5}),
]
for fmt, args, kwargs in FORMAT_MAP_TESTS:
    struct = _struct.Struct(fmt)
    try:
        struct.format_map(kwargs)
    except ValueError as e:
        print("Error in format_map({!r}): {!r}".format(fmt, e))
    else:
        try:
            struct.pack(*args, **kwargs)
        except TypeError as e:
            print
