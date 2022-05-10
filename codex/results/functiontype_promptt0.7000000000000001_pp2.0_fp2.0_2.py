import types
# Test types.FunctionType
def func_execute(func, times):
	for i in range(times):
		func()
# Test types.LambdaType
def lambda_execute(func, times):
	for i in range(times):
		func()

a = lambda: print("Hello")
print("TEST START:")
print("TEST 1:")
func_execute(a, 10)
print("TEST 2:")
lambda_execute(a, 10)
print("TEST END")
'''
