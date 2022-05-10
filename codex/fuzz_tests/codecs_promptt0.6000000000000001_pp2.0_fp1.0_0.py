import codecs
# Test codecs.register_error
class my_error(Exception):
    pass
def my_error_handler(exception):
    return (u"", exception.end)
codecs.register_error("my_error", my_error_handler)
def my_decode(input, errors='strict'):
    raise my_error
codecs.register(my_decode)
# 1st test: error handler given as name
try:
    b("123").decode("my_decode", "my_error")
except my_error:
    pass
# 2nd test: error handler is callable
def handler(exception):
    return ("", exception.end)
try:
    b("123").decode("my_decode", handler)
except my_error:
    pass
# 3rd test: error handler is a tuple
try:
    b("123").decode("my_decode", ("ignore", handler))
except my_error:
    pass
# 4th test: error handler is a dictionary
try:
    b("123").decode("my_decode", {"error":
