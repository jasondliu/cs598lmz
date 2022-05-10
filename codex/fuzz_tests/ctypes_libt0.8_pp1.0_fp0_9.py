import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")



def strHex(text):
    #it returns a string in hexadecimal format
    return text.encode("hex")


def strUnhex(text):
    #it returns a string in hexadecimal format
    return text.decode("hex")


def list_eq(lista,listb):
    #a function to compare two lists
    if len(lista)!=len(listb):
        return False
    for i in xrange(len(lista)):
        if lista[i]!=listb[i]:
            return False
    return True


#defining a function to find the index of an element of a list
def index(l, e):
    #l is a list, e is an element
    try:
        return l.index(e)
    except ValueError:
        pass
    for i in xrange(len(l)):
        if l[i]==None:
            return i
    return -1



