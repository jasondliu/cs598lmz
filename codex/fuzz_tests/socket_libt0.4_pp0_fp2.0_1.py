import socket
import threading
import time
import sys

# Variables

# Clase para el servidor
class Servidor():
	# Constructor de la clase
	def __init__(self, host="localhost", port=9999):
		# Creamos el socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((host, port))
		self.sock.listen(10)
		self.sock.setblocking(False)
		
		# Lista de clientes
		self.clientes = []
		
		# Hilo para aceptar conexiones
		aceptar = threading.Thread(target=self.aceptarCon)
		aceptar.daemon = True
		aceptar.start()
	
	# Funcion para aceptar
