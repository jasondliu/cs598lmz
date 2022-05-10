import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()


def realizar_comparaciones_de_puedo_eliminar_elementos(matriz):
    # Preguntamos si la parte de arriba puede ser borrada.
    print("Preguntamos si la fila puede ser borrada:")
    fila = random.randint(0, len(matriz) - 1)
    print("fila: ", fila)
    if puede_borrar_fila(matriz, fila):
        print("Puede ser borrada la fila: ", fila)
    else:
        print("No puede ser borrada la fila: ", fila)

    # Preguntamos si la parte de la izquierda puede ser borrada.
    print("Preguntamos si la fila puede ser borrada:")
    columna = random.randint(1, len(matriz[0]) - 1)
    print("colum
