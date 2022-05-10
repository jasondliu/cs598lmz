import types
types.FunctionType
type(synched)

def named(**kwargs):
    print(kwargs)
    
    
named(name='red',age=23)

def named_2(**kwargs):
    print(kwargs)
named_2(name='bob',age=20)

def print_nicely(**kwargs):
    named(**kwargs)
    print('I would like to have a '+kwargs['food'])
    
print_nicely(food='lunch',drink='cola')

def both(*args,**kwargs):
    print(args)
    print(kwargs)
    
both(1,3,5,7,9,name='Bob',job='dev')

t=(1,3,5,7,9)
d={'name':'bob','job=':'dev'}

a, b, c, d, e = t
a,c,e

d = {'name':'Bob','Job':'Dev'}
for k in d:
    print(k)

