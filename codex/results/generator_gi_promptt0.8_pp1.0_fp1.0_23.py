gi = (i for i in ())
# Test gi.gi_code is None

gi = (i for i in ())
# Test gi.gi_code is not None

gi = (lambda : (yield))()
# Test gi.gi_code is not None

gi = (lambda : (yield))()
# Test gi.gi_code is not None

gi = (lambda : (yield))()
# Test gi.gi_code is not None

gi = (lambda : (yield))()
# Test gi.gi_code is not None
