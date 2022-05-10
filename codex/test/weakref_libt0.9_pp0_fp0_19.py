import weakref

class CounterA(metaclass=TypeMeta):
    _attr=['__it_counter']

    def __init__(self):
        self.__it_counter=0

    def __next__(self):
        if self.__it_counter>=10 : raise StopIteration
        ret=self.__it_counter
        self.__it_counter+=1
        return ret

###############################################################################
# Attention : il n'y a pas de test de type pour les types de retour de méthodes !!
###############################################################################
class CounterB(metaclass=TypeMeta):
    _attr=['__it_counter']
    def __init__(self):
        self.__it_counter=0

    def __next__(self):
        if self.__it_counter>=10 : return
        ret=self.__it_counter
        self.__it_counter+=1
        return ret

###############################################################################
class CounterC(metaclass=TypeMeta):
    _attr=['__it_counter']
