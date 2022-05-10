import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("d:\\projectdata\\python\\stock\\stock.db") con = sqlite3.connect("d:\\projectdata\\sqlite\\stock_test.db"). It's work.

# 20180701. Check exception error. 

class SingletonInstace:
    def __init__(self):
        self.con = sqlite3.connect("d:\\projectdata\\sqlite\\stock_test.db")
        #self.con = sqlite3.connect(":memory:")
        self.__lock=threading.RLock()
    
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst=super(SingletonInstace,cls).__new__(cls,*args,**kwargs)
        return cls._inst
    
    def GetConnection(self):
        return  self.con;
    
    def __del__(self):
        self.con.close()

def test_func():
    #test_Singleton_Instance()
   
