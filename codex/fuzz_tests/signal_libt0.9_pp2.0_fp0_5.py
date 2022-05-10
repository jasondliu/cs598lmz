import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import gobject, gtk, gtk.glade
import random, pygame
import socket
from pygame.locals import *
from threading import Thread
from pysqlite2 import dbapi2 as sqlite


socket.setdefaulttimeout(2)

class Cliente(Thread):
	def __init__(self,ip,usuario):
		Thread.__init__(self)
		self.usuario=usuario
		self.info=''
		self.nombre=""
		try:
			self.con=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.con.connect((ip,8000))
			self.con.send("crear")

			self.listo=0
			
			self.terminar=False # variable para realizar el cierre del socket. OJO
			self.start()
		except:
	
