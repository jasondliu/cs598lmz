import threading
threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)

#Informacion Tic tac toe
FirstPlayer = ""
SecondPlayer = ""
Piece = ""
Player = ""

#Informacion del usuario
Nombre = ""
Email = ""
Password = ""

#Informacion de la partida
GameID = 0
Turno = ""
PlayerSee = ""
TileValues = []
UndoPositions = []

#Informacion de la partida Temporal
Temp_Turno = ""
Temp_PlayerSee = ""
Temp_TileValues = []
Temp_GameID = 0
CantidadMovimientos = 0

#Constantes para la interfaz
Tamano = 500
Margen = Tamano * 0.05
Ancho = Tamano * 0.1
COLUMNAS = 3
FILAS = 3

#Constantes
#Estatus de la partida
TURN_PLAYER1 = 1
TURN_PLAYER2 = 2
TURN_PLAYER1_WIN = 3
TURN
