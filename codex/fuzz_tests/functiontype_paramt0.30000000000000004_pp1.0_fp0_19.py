from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda') for i in range(10))

# test_list_comprehension_with_generator_expression
list(i for i in range(10))

# test_list_comprehension_with_generator_expression_and_if
list(i for i in range(10) if i % 2 == 0)

# test_list_comprehension_with_generator_expression_and_if_else
list(i if i % 2 == 0 else -i for i in range(10))

# test_list_comprehension_with_generator_expression_and_if_elif_else
list(i if i % 2 == 0 else -i if i % 3 == 0 else i * 2 for i in range(10))

# test_list_comprehension_with_generator_expression_and_if_elif_else_with_no_else
list(i if i % 2 == 0 else -i if i % 3 == 0 else i * 2 for i in range(10) if i % 5 ==
