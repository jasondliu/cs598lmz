fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError as e:
    print(e)

# test_generator_expression_in_lambda
fn = lambda: (i for i in ())
try:
    fn()
except TypeError as e:
    print(e)

# test_simple_generator_expression
g = (i for i in ())
print(g)

# test_simple_generator_expression_with_tuple
g = (i for i in (1, 2, 3))
print(g)

# test_simple_generator_expression_with_tuple_and_name
g = (i for i in (1, 2, 3))
print(g)

# test_simple_generator_expression_with_tuple_and_name_and_return
g = (i for i in (1, 2, 3))
print(g)

# test_simple_generator_expression_with_tuple_and_name_and_return_with_parens
g = (i for i in (1, 2, 3))
