from types import FunctionType
list(FunctionType(dict(__globals__=dict(__name__='_'))['__globals__'].values()))

# eval is a bad idea. As it might be able to run as superuser.
eval(dict(__globals__=dict(__name__='_'))['__globals__']['__getitem__']('__name__'))

# What is __class__
# Sometimes, you can get arbitrary code execution by changing __class__ of some object
# into some other arbitrary class

# This is an example of a security hole in Python
# If you have a web app, it might be calling eval() on user input
# For example:
#  eval(request.get('user_input'))
#  This allows an attacker to run any code they want
#
#  If a web app allows this, to protect itself, it should define what functions and classes are
#  allowed for the function to use
#  For example:
#   eval(request.get('user_input'), dict(pow=pow, sqrt=sqrt))
#  This allows
