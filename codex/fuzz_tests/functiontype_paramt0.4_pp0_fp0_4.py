from types import FunctionType
list(FunctionType(lambda: None, globals(), '<lambda>') for _ in range(2))

# test_list_comprehension_in_tuple
tuple(i for i in range(5))

# test_list_comprehension_in_dict
{i: i for i in range(5)}

# test_list_comprehension_in_set
{i for i in range(5)}

# test_list_comprehension_in_dict_comprehension
{i: j for i in range(5) for j in range(5)}

# test_list_comprehension_in_set_comprehension
{i for i in range(5) for j in range(5)}

# test_list_comprehension_in_yield
def f():
    yield from (i for i in range(5))

# test_generator_expression_in_list
list(i for i in range(5))

# test_generator_expression_in_tuple
tuple(i for i in range
