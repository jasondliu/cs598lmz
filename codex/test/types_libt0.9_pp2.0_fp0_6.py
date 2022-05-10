import types
types.FunctionType

## LAB(end solution)

## LAB(begin bonus)
# Q10: Add a *method* 'is_polynomial' to the Polynomial class constructed above.
# Your method should return True if the Polynomial can be expressed as a
# polynomial and False otherwise.
def is_polynomial(self):
    """Returns True if this polynomial is a valid polynomial
    in a single variable, and False otherwise.
    """
    #YOUR CODE HERE
    types.MethodType
    return True

Polynomial.is_polynomial = is_polynomial

# Q11: Add a *class*method 'identity' to the Polynomial class constructed above.
# Your method should take a single positive integer N and return the
# polynomial object representing the identity polynomial x^N for that value
# of N.
def identity(cls, n):
    """Returns the identity polynomial x**n
    """
    #YOUR CODE HERE
