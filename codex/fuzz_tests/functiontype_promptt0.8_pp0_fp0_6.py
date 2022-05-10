import types
# Test types.FunctionType()
def return_true():
    return True
# Check
isinstance(return_true, types.FunctionType)

# Test types.LambdaType()
return_true_lambda = lambda: True 
# Check
isinstance(return_true_lambda, types.LambdaType)

# Test types.GeneratorType()
def square_numbers(nums):
    for i in nums:
        yield (i * i)
# Check
isinstance(square_numbers(range(5)), types.GeneratorType)

# Test types.TracebackType()
def get_stack_trace():
    return traceback.format_stack()
# Check
isinstance(get_stack_trace(), types.TracebackType)

# Test types.FrameType()
def function_that_calls_trace():
    traceback.print_stack(frame=None, limit=None)
# Check
isinstance(function_that_calls_trace(), types.FrameType)

# Test types.CodeType()
def get_code_object(func):
   
