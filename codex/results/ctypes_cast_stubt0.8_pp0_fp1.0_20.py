import ctypes
ctypes.cast(id(obj), ctypes.py_object).value
#copies list 
L = [1,2,3]
X = L * 4
Y = [L] * 4
print(L)
print(X)
print(Y)

L[1] = 0
print(L)
print(X)
print(Y)
#end
#####Keys and Values
#VIEWS
D = {'a':1, 'b':2, 'c':3}
K = D.keys()
V = D.values()
K[1] #Error 
#D['b'] = 0
#print(K)
#print(V)
#list(K)
print(list(K))
print(list(V))

#for key in K:
#    print(key + '=>' + str(D[key]))

for value in V:
    print(value)
#END

#####
print(D)
print(D.items())
for K, V in D.items():
    print(K,V)
#END


