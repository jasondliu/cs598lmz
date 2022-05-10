import _struct
# Test _struct.Struct

def get_struct_test_data():
    import random
    import sys
    import time
    import struct

    # Create a list of random numbers, to be packed according to fmt.
    # Use the same numbers for all formats to test pack's consistency.
    n = 10
    randints = list(range(n))
    random.shuffle(randints)
    # Use a fixed seed, so tests are reproducible
    random.seed(123)
    randfloats = [random.random() for i in range(n)]
    randints2 = list(range(-n, 0))
    random.shuffle(randints2)
    randfloats2 = [random.random() for i in range(-n, 0)]
    randbytes = list(range(n))
    random.shuffle(randbytes)
    randbytes2 = list(range(-n, 0))
    random.shuffle(randbytes2)

    # Assumes native mode.
