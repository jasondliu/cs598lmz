from types import FunctionType
list(FunctionType(lambda: 0, {}, "return"))

# calling lambda without params.
ux = (lambda: 2)()

# lambda with if else.
cond_lambda = (lambda x : 2 if x > 2 else 1)

# Lambda with multi conditions.
add_lambda = (lambda x, y : x if x > 0 else y)

# Lambda inside a list.
lam_in_list = [lambda: 0]

# Lambda inside lambda.
lam_in_lam = (lambda y: lambda: y)

# curly brackets in lambda.
curly_br = (lambda {'x'}: 0)

# lambda as decorator.
lam_dec = (lambda x: x ^ (x * 2))(2)

# lambda + complex.
lambda_complex = (lambda x: (lambda y: y)(x))(3j)

# lambda with and.
and_lam = (lambda x, y: x and y)

# lambda with class parenthesis.
class_lam = (lambda x, y: x)(2)(3)

# lambda with comparisons
