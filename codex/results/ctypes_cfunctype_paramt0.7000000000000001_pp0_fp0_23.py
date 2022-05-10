import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)

from pymongo import MongoClient
from utilities import printDictList,printDict,getDictList,getDict
from time import time
from getpass import getpass
from sys import argv,exit
from os.path import exists

from utilities import str2bool, getDictList, getDict, printDictList, printDict, Dict, DictList, DictTree
from sys import argv,exit

from os import system
from getpass import getpass
from utilities import str2bool
from pymongo import MongoClient
from os.path import exists
from utilities import str2bool, getDictList, getDict, printDictList, printDict, Dict, DictList, DictTree
from pymongo import MongoClient, DESCENDING
from utilities import printList, printDict, printDictList, getDictList, getDict, Dict, DictList, DictTree
from time import time
from sys import exit, argv
from os.path import exists,split,absp
