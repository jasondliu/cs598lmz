from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a,b)
print(a)
print()

print([x for x in a])
print([x for x in b])

# Para ver la funcion que genera el generador:
print()
print(a.__next__) # Funcion que genera los valores
print(a.__next__.__closure__) # Acceso a la funcion de cierre (clausura)
print(a.__next__.__closure__[0].cell_contents) # Acceso a la lista

# ----------- Funciones dentro de funciones:
def f1(x1):
    def f2(x2):
        return x2 + 2
    return x1 + f2(x1)
print()
print(f1(1))
print(f1(x1=5))
print()

# Ejemplo:
def nested_func(n):
    def return_x(x):
        return x ** n
    return return_x

