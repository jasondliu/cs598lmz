import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return ("", exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

s = "abc\u20acdef"
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii", "test.my_error_handler"))
print(s.encode("ascii",
