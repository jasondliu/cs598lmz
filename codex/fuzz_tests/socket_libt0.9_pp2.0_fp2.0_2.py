import socket
import sys
import threading

class Cliente(threading.Thread):

    def __init__(self, addr, socketCliente):
        threading.Thread.__init__(self)
        self.addr = addr
        self.socketCliente = socketCliente
        self.pong = 0
        self.salir = False
        self.nombre = ''
        self.start()

    def run(self):
        print('Conectado a [' + str(self.addr[0]) + ':' + str(self.addr[1]) + ']')
        self.socketCliente.send(b'Nombre:')
        self.nombre = self.socketCliente.recv(1024).decode('utf-8')
        self.socketCliente.send(('Bienvenido ' + self.nombre + '!').encode('utf-8'))
        while True:
            datos = self.socketCliente.recv(1024).decode('utf-8')

            if datos == 'q':
                self.sal
