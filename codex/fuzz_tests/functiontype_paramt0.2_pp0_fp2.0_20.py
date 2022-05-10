from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda') for x in range(10))

# A lambda function that returns a lambda function
(lambda x: (lambda y: x + y))(1)

# A lambda function that returns a lambda function that returns a lambda function
(lambda x: (lambda y: (lambda z: x + y + z)))(1)(2)

# A lambda function that returns a lambda function that returns a lambda function that returns a lambda function
(lambda x: (lambda y: (lambda z: (lambda w: x + y + z + w))))(1)(2)(3)

# A lambda function that returns a lambda function that returns a lambda function that returns a lambda function that returns a lambda function
(lambda x: (lambda y: (lambda z: (lambda w: (lambda v: x + y + z + w + v)))))(1)(2)(3)(4)

# A lambda function that returns a lambda function that returns a lambda function that returns a lambda function that returns a lambda function that returns a lambda function
(lambda x: (lambda y: (lambda z: (lambda w: (lambda v
