import socket
socket.if_indextoname(3)

import socket
socket.if_indextoname(4)

#Realiza una función que devuelva una lista con las direcciones de red de la máquina.
import socket
def lista_interfaces():
    lista = []
    for i in range(10):
        try:
            lista.append(socket.if_indextoname(i))
        except:
            pass
    return lista

lista_interfaces()

#Realiza una función que devuelva una lista con los nombres de los adaptadores de red de la máquina.
import socket
def lista_interfaces():
    lista = []
    for i in range(10):
        try:
            lista.append(socket.if_indextoname(i))
        except:
            pass
    return lista

lista_interfaces()

#Realiza una función que devuelva una lista con las direcciones IP de los adaptadores de
