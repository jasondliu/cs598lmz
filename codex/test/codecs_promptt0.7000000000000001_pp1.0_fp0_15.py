import codecs
# Test codecs.register_error
import string

def uchr(i):
    return unichr(i)

def main():
    # Try with a non-unicode error handler
    try:
        codecs.register_error(str, codecs.replace_errors)
    except TypeError:
        pass
