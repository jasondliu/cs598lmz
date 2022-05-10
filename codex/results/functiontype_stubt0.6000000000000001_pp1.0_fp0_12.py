from types import FunctionType
a = (x for x in [1])
a.next()

def test_fn():
  return 1

test_fn()

test_fn.__name__

# https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string

def test_fn2():
  return 2

test_fn2()

def get_test_fn():
  return test_fn2

get_test_fn()
get_test_fn()()

def get_test_fn_str():
  return "test_fn2"

get_test_fn_str()

def get_test_fn_str_lambda():
  return lambda: "test_fn2"

get_test_fn_str_lambda()

def get_test_fn_str_lambda_callable():
  return lambda: "test_fn2"

get_test_fn_str_lambda_callable()()

def get_test_fn_str_lambda_callable2():
  return lambda: test_
