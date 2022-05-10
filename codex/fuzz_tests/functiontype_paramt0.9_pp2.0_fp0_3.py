from types import FunctionType
list(FunctionType(anonymous_lambda_generator, globals(), name="AnonymousLambda"))

# First use case:
# Higher-order functions
def higher_order_func(action, values):
    """Higher order function, pass a function and a list to iterate
    and apply this function to all elements of this list.
    """
    return [action(value) for value in values]

add_ones = lambda element: element + 1 if element < 3 else element
higher_order_func(add_ones, [1, 2, 3, 4])

# Second use case:
# Passing local variables to lambdas
def execute_one_time(action, value):
    """
    Pass a function created with a lambda to a function
    """
    return action(value)

def pass_variable_to_lambda():
    VARIABLE = "Value from outer scope"
    execute_one_time(lambd
