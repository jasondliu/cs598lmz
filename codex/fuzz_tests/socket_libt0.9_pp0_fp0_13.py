import socket
import libreriacompleja

#Set to connect to socket
port = 8000
host = 'localhost'

#creacion de socket
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((host, port))

#mensaje para empezar
mensaje2 = "Bienvenido al Servicio de Operaciones Complejas, ingrese la opcion que desee ejecutar:\n\
1)Suma\n\
2)Resta\n\
3)Multiplicacion\n\
4)Division\n\
5)Raiz\n\
6)Exponenciacion\n\
7)Comparar dos numeros complejos\n\
8)Conjugado\n\
9)Pasar a Cartecianas\n\
10)Pasar a polar"


print mensaje2
socket1.send(mensaje2)


while True:
	#capturar el dato de teclado
	numero =
