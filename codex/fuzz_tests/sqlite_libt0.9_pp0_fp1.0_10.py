import ctypes
import ctypes.util
import threading
import sqlite3
import time
import random

# Lists for holding letters for any given game
A_list = ['A','a','4','@','^','&','*','#','1','X','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
X_list = ['X','x','X','x','0','o','O','%','^','&','*','#','(',')','1','x','x','x','x','x','x','x','x','x','x','x']
F_list = ['F','f','F','f','|=','|-|','VV','vv','vV','Vv','=)','=|','z','o','O','-=','x','x','x','x','x','x','x','x','x','x']
E_list = ['E','e','e','e','E','|=','|-|','vv','VV','=)','=|','3','3','z','o','O','-=','x','x','x','x','x','x','
