gi = (i for i in ())
# Test gi.gi_code
print(test_gi.gi_code)
print(iter(test_gi))

# Example: Getting back the code of a generator created by genexpr
test_ge = ([i, i] for i in [1, 2, 3, 4])
print(test_ge.gi_code)
print(iter(test_ge))


# Generator using __name__ attribute
def try_gen():
    while True:
        try:
            yield
        except Exception as e:
            print(e)
            break

# Generate exception: NameError Exception
try_gen_ex = try_gen()

print(next(try_gen_ex))
try_gen_ex.throw(Exception, "Exception 1")
print(next(try_gen_ex))
try_gen_ex.throw(Exception, "Exception 2")
print(next(try_gen_ex))

# Generator using __qualname__ attribute
def try_gen():
    try:
        yield
    except Exception as e:
        print(e)

# Generate exception: NameError Exception
try_
