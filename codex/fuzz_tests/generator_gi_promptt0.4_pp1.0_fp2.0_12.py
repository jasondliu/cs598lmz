gi = (i for i in ())
# Test gi.gi_code is None

gi = (i for i in (1, 2, 3))
# Test gi.gi_code is not None

gi = (i for i in (1, 2, 3)).__iter__()
# Test gi.gi_code is not None

gi = (i for i in (1, 2, 3)).__iter__().__iter__()
# Test gi.gi_code is not None

gi = (i for i in (1, 2, 3)).__iter__().__iter__().__iter__()
# Test gi.gi_code is not None

gi = (i for i in (1, 2, 3)).__iter__().__iter__().__iter__().__iter__()
# Test gi.gi_code is not None

gi = (i for i in (1, 2, 3)).__iter__().__iter__().__iter__().__iter__().__iter__()
# Test gi.gi_code is not None

gi = (i for i in (1, 2, 3)).__iter__().__iter__().__
