gi = (i for i in ())
# Test gi.gi_code.Ý The code attribute does not exist for a
# generator. Not sure wheather this is a bug or a feature.
# gi.gi_frame.f_code == None


def g():
    x = 1
    yield x
    yield x
gi = g()
gi.gi_frame.f_code == g.func_code
gi.next()
gi.next()

# The following generator returns square roots of numbers in the
# range of 1 to the number of items requested.
# The code uses two yield statements with one of the statements used
# to send back results and the other to send back exceptions.
# The generator is parametrized with the number of items which it should
# return.

class Result: pass

def square_root_generator(num):
    k = 0
    result = Result()
    try:
        for i in range(num):
            k = k + 1
            result.value = math.sqrt(k * k)
            yield result
    except Exception as err:
        result.exc = err
        yield result

def __main
