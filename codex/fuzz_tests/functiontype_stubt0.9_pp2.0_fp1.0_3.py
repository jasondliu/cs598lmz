from types import FunctionType
a = (x for x in [1])
# isinstance(a,FunctionType)
o = [1,2]
username = [0,0,0]

def uuuuu(usernameprinter):
    def run(x):
        return usernameprinter(username)
    return run

@uuuuu
def userprinter(x):
    print x

userprinter(username)
