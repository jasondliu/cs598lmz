import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return "hi"
    def write(self, val):
        return len(val)
    def flush(self):
        return
    def close(self):
        return

# Creating string class wrapper
class Str(str):
    def __and__(self, other):
        return self + ' ' + other
    def __or__(self, other):
        return self + other


# Write a decorator @file_check which will check for file existence
def file_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if os.path.isfile(args[0]):
            return func(*args, **kwargs)
        else:
            return False
    return wrapper

# Write a decorator @debug which will print the arguments passed
# to the function before calling it
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return func(*
