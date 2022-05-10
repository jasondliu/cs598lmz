import io
class File(io.RawIOBase):
    def close(self):
        p()
        pass

f = File()
try:
    print("try")
finally:
    print("finally close")
    f.close()

def echo():
    pass
    #class Echo(object):
    #    pass
    #return Echo()
def echo1(p,q):
    return p + q
s = echo()
print(s)

def print_me(f):
    print(f)

def greet(func):
    print("123")
    func("not what you want")
    return func
@greet
def print_me(s="abc"):
    print(s)

print(__file__)
print(__name__)
print(__doc__)
print(__name__)
print(__package__)
print(__loader__)

# type annotation
# use add :
# pip install --user pytype

# try except
try:
    pass
except:
    pass
    #except Exception as e
    pass
    # AttributeError,
