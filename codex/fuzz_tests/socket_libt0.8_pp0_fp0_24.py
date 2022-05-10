import socket
import threading
import time
import unicodedata
import sys

class Paquete:
    """Paquete para envio y recepcion por sockets"""
    
    def __init__(self,data,tipo):
        self._tam = len(data)
        self._data = data
        self._tipo = tipo
    
    def recibir(self,socket):
        #Leemos el la cabecera con el tamano
        cabecera = socket.recv(8)
        
        if len(cabecera) == 0:
            #Conection closed
            return None
        
        while len(cabecera) < 8:
            #Vamos a por mas datos
            cabecera += socket.recv(8 - len(cabecera))
        
        self._tam = int(cabecera)
        
        self._tipo = socket.recv(1)
        
        self._data = ""
        
        while len(self._data) < self._tam:
            #V
