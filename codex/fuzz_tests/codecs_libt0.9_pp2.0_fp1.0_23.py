import codecs
codecs.register(CustomUTF8)

archivo = open("archivo.txt", "w")
archivo.write("cadena")
archivo.close()

archivo = codecs.open("archivo.txt", "w", "utf_8_sig")

archivo.write("cadena")
archivo.close()
