gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# gi_frame is NULL
assert(gi.gi_frame is None)

# Using Mix generator and generator expressions

def gen_example(N):
    for i in range(N):
        yield i

#y = sum(n for n in range(N)) + sum(n for n in gen_example(N))

print("Done!")
