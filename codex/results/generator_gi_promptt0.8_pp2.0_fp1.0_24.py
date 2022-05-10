gi = (i for i in ())
# Test gi.gi_code.co_name == 'gi'
print("Test gi.gi_code.co_name == 'gi':", gi.gi_code.co_name == 'gi')
print("Test next(gi) raises StopIteration:", _expect_exception(StopIteration, next, gi))
print("Test 3 in gi raises TypeError:", _expect_exception(TypeError, 3 in gi))
print("Test gi[0] raises TypeError:", _expect_exception(TypeError, lambda: gi[0]))

print("Test next(gi) raises StopIteration:", _expect_exception(StopIteration, next, gi))

# Test gi.gi_code.co_name == 'gi'
print("Test gi.gi_code.co_name == 'gi':", gi.gi_code.co_name == 'gi')



def rec(x):
    if x < 5:
        return [x, rec(x + 1)]
    else:
        return x

print("Test rec(
