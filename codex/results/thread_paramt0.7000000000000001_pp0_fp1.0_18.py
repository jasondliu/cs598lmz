import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hola, mundo.")).start()

#Ejemplo de hilos con argumentos
import threading
def hilo_argumentos(valor):
    print("Soy el hilo {} y mi argumento es {}.".format(threading.current_thread().name, valor))

threads = [threading.Thread(target=hilo_argumentos, args=(i,)) for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

#Ejemplo de hilos con argumentos
import threading
def hilo_argumentos(valor):
    print("Soy el hilo {} y mi argumento es {}.".format(threading.current_thread().name, valor))

threads = [threading.Thread(target=hilo_argumentos, args=(i,)) for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

#Ejemplo de hilos
