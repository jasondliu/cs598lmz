from types import FunctionType
list(FunctionType('f',globals())(x for x in range(6)))

#TODO: http://stackoverflow.com/questions/28124960/how-to-use-generator-expressions-python-as-right-side-of-assignment
#TODO(gigatron): figure out how to effectively mutate a list by name.  Not sure if i like.
def lmod(L):
    L=[]
    #L.append(100)


#TODO(gigatron): figure out how to 'makelocal' a list by name.  Not sure if i like.
def lmodr(L=None):
    if L==None:
        L=[]
    return L

def hello(x,y):
    def f(z):
        return z**2
    x=x+y+f(x)+f(y)
    return x
hello(1,2)

print("\n###### Wackstack ######\n")

class Wackstack(list):
    def push(self,x):
        self
