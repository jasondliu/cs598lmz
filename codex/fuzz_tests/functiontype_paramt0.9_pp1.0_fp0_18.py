from types import FunctionType
list(FunctionType(lambda: None))

# Try this.
# f = lambda: None
# print(type(f))  # ---> <class 'function'>

# Functional decorators
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper


@p_decorate
def get_text(name):
   return "<h1>" + name + "</h1>"

flask = get_text('Flask')
print(flask)

# Practical decorator
def logger(func):
   def log_wrapper(*args, **kwargs):
       print('DISPLAY: ' + func.__name__ +
             " was called")
       return func(*args, **kwargs)
   return log_wrapper


@logger
def display_info(name, age):
   print('display_info ran with arguments \
		({}, {})'.format(name, age))

display_info('Sagar', 23)

# Practical decorator with args
