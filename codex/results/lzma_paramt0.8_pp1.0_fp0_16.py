from lzma import LZMADecompressor
LZMADecompressor().decompress(open("test.bin").read())

#4 Kompresja
#Zad 1
#Metoda Shannon’a fanno znajdywania najbardziej prawdopodobnych następników na podstawie dotychczasowych grup znaków tzn.
#wskaźnik Shannon’a dla danego"zdjęcia"grupuje znaki w oparciu o ich prawdopodobieństwo wystąpienia.

#Zad 2
import array
import math

def entropy(s):
    p, lns = Counter(s), float(len(s))
    return -sum(count/lns * math.log(count/lns, 2) for count in p.values())

#Zad 3
import ctypes

def entropy_array(a):
    p, lns = Counter(a), float(len(a))
    return -sum(count/lns
