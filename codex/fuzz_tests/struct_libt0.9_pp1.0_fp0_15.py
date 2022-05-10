import _struct

# Clase de cada nodo de la lista
class ComponentesLS:

    def __init__(self, cp=None, sig=None):
        self.cp = cp
        self.sig = sig

# Clase de la lista simple
class ListaSimple:
    def __init__(self):
        self.inicio = None
        self.tamano = 0

    # Método para agregar un nuevo elemento
    def insertarAlFinal(self, cp):
        if self.inicio == None:
            self.inicio = ComponentesLS(cp, None)
        else:
            aux = self.inicio
            while aux.sig != None:
                aux = aux.sig

            aux.sig = ComponentesLS(cp, None)
        self.tamano += 1

    # Método para eliminar la figurita en la posicion ingresada
    def eliminarFigurita(self, posicion):
        if self.inicio == None:
            print("No existen figuritas en la
