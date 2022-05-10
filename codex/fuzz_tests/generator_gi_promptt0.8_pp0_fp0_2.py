gi = (i for i in ())
# Test gi.gi_code
gi.gi_code

# Test gi.gi_frame
if hasattr(gi, 'gi_frame'):
    gi.gi_frame

# Test gi.gi_running
if hasattr(gi, 'gi_running'):
    gi.gi_running

# Test gi.gi_yieldfrom
if hasattr(gi, 'gi_yieldfrom'):
    gi.gi_yieldfrom

# Test next(gi)
if hasattr(gi, 'gi_frame'):
    # Only run this test if gi_frame is present - should not be present in
    # optimized builds
    try:
        next(gi)
    except ValueError:
        # ValueError("generator already executing")
        pass
    except StopIteration:
        pass

l = [1, 2, 3]
gi = (i for i in l)
# Test gi.gi_code
gi.gi_code

# Test gi.gi_frame
if hasattr(gi, 'gi_frame'):
    gi.
