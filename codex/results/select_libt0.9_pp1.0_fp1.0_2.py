import select, os, socket, sys, errno, time, signal, json, traceback, pickle
import pathlib, stat, getpass, logging, traceback, hashlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / 'procs'))
import procs.nmap, procs.passwords_shortlist, procs.portscan, procs.crawl
import procs.myfile

class fserv:
    def __init__(self, verbose):
        self.verbose = verbose
        self.procs_obj = None
        self.procs_file = None

        self.SERVER_ADDR = ''
        self.SERVER_PORT = 0

        self.__myobj = { None, }
        self.__crawlobj = { None, }
        self.__start_time = [None,]
        self.__ind = 0

        # log
        if self.verbose:
            self.logger = logging.getLogger(__name__)
            self.logger.set
