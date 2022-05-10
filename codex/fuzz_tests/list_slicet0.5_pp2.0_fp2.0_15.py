import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

'''

#print(run_code(code))

#code = '''
#def f(x):
#    return x*2
#'''

#print(run_code(code))

#code = '''
#def f(x):
#    return x*2
#'''

#print(run_code(code))

#code = '''
#def f(x):
#    return x*2
#'''

#print(run_code(code))

#code = '''
#def f(x):
#    return x*2
#'''

#print(run_code(code))

#code = '''
#def f(x):
#    return x*2
#'''

#print(run_code(code))

#code = '''
#def f(x):
#    return x*2
#'''

#print(run_code(code))

#code = '''
#def f(x):
#    return x*2
#''
