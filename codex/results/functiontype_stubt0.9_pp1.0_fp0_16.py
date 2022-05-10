from types import FunctionType
a = (x for x in [1])
type(a)

isinstance((x for x in [1]), list)
type((x for x in [1]))
type(make_random_function(2))
# 2 is the number of arguments in the func

type(square)
type(cube)

# Now we're going to create a function that generates 2-argument functions that act like our input generator
# and returns the modified function.

def make_generator_from_function_and_inverse_function(f, f_inv):
    # This function takes two functions: f and f_inv, where f_inv is an inverse of f
    # i.e. f_inv(f(x)) == x
    # It returns a 1-argument function that is a generator and goes f, f_inv, f, f_inv, ...
    def generator(x):
        while True:
            yield f(x)
            x = f_inv(x)
    return generator
        
def double(x):
    return 2 * x

def halve(x):
    return x / 2
    
print double
