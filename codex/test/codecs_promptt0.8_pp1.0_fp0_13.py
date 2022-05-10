import codecs
# Test codecs.register_error
a = (1, 2)
try:
    raise ValueError(*a)
except ValueError as e:
    print("Exception:", e)
