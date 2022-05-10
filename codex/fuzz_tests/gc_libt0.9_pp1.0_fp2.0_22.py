import gc, weakref

from classes.CachedDictFile import CachedDictFile
from classes.Logger import Logger
from classes.Configuration import Configuration
from classes.Storage import Storage
from classes.MediaItem import MediaItem
from classes.HTTPServer import HTTPServer
from functions import *
from classes.UpdateThread import UpdateThread
from classes.TVDBSession import TVDBSession


def main():

	init()
	config = Configuration()
	logger = Logger(config)
	
	#config.setdefault('server.name', str(socket.gethostname()))
	#config.setdefault('server.port', 8080)
	#config.setdefault('update.modified', True)
	#config.setdefault('update.scan', True)
	
	
	if not config.getboolean('update.scan') and not config.getboolean('update.modified'):
		logger.log('Nothing to do, exiting', Logger.INFO)
		sys.exit(0)
	
	
	# Initializations
	
	if not config.get('server
