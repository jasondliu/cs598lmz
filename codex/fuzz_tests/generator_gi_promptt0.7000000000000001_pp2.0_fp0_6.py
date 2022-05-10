gi = (i for i in ())
# Test gi.gi_code.co_code
if hasattr(gi, 'gi_code'):
    code = gi.gi_code
    if hasattr(code, 'co_code'):
        print(code.co_code)

# Test gi.gi_frame.f_code.co_code
if hasattr(gi, 'gi_frame'):
    frame = gi.gi_frame
    if hasattr(frame, 'f_code'):
        code = frame.f_code
        if hasattr(code, 'co_code'):
            print(code.co_code)
