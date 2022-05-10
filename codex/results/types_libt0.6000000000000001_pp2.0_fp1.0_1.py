import types
types.FunctionType(lambda: None, globals())

# crea una función con un nombre
def f(): pass
f

# asigna la función a una variable
g = f
g

# asigna la función a un atributo
f.attr = 42
f.attr

# asigna la función a un ítem de diccionario
d = {}
d[42] = f
d[42]

# asigna la función a un elemento de una lista
l = []
l.append(f)
l[0]

# pasa la función a una función
def h(func): return func
h(f)

# retorna la función de una función
def j(): return f
j()

# retorna la función de una función que retorna una función
def k(): return h
k()(f)

# pasa la función a una función que ret
