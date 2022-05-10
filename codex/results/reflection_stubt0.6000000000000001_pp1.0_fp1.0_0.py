fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_invalid_yield_as_stmt()
# test_invalid_yield_as_stmt_with_arg()
# test_invalid_yield_as_expr()
# test_invalid_yield_as_expr_with_arg()

# test_syntax_error()
# test_type_error()
# test_type_error_2()
# test_value_error()
# test_value_error_2()
