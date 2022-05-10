from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("/Users/aldemaro/Documents/python/file.bz2", "rb").read())

# Abrir un archivo y escribir en el
file = open("/Users/aldemaro/Documents/python/file.txt", "w")
file.write("Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.")
file.close()

# Abrir un archivo y leerlo
file = open("/Users/aldemaro/Documents/python/file.txt", "r")
print(file.read())
file.close()

# Abrir un archivo y leer sólo las primeras 10 líneas
file = open("/Users/aldemaro/Documents/python/file.txt", "r")
print(file.readlines(10))
file.close()

# Abrir un archivo y leerlo con una variable
with open("/Users/aldemaro/Documents/python/
