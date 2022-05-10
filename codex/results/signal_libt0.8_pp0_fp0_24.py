import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

##
## @brief      Funcion para crear archivos
##
## @param      path  The path
## @param      text  The text
##
## @return     True si se creo correctamente, False en caso contrario
##
def createFile(path):
	try:
		file = open(path, "w")
		file.close()
		return True
	except:
		return False

##
## @brief      Funcion que borra un archivo
##
## @param      path  The path
##
## @return     True si se borro, False en caso contrario
##
def deleteFile(path):
	try:
		os.remove(path)
		return True
	except:
		return False

def setNewAddress(path, address):
	createFile("config.conf.tmp")
	if not deleteFile("config.conf"):
		return False
	try:

