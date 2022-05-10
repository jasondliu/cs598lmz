gi = (i for i in ())
# Test gi.gi_code is NULL.
gi.gi_code = None
gi.gi_frame = None
gi.gi_running = 0
gi.gi_yieldfrom = None
gi.gi_weakreflist = []

# The sequence of values to be returned by the generator.
values_to_return = [42, 'hello world', None]
# The number of values returned by the generator so far.
i = 0

def my_generator():
    # The generator's code.
    global i
    while True:
        # Yield the next value from the sequence.
        yield values_to_return[i]
        i += 1
        # Stop the generator when all values have been returned.
        if i >= len(values_to_return):
            break

# The 'gi_frame' attribute of the generator-iterator is set to the current
# frame object when the generator is created.
gi.gi_frame = my_generator.__code__

# When the generator is resumed by the 'yield from' expression, the
# 'gi_code' attribute of the generator-iterator is set
