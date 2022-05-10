import threading
threading.stack_size(2*1024*1024)

import MySQLdb
from DBUtils.PooledDB import PooledDB

import pymongo
from bson.objectid import ObjectId

from datetime import datetime


class DBClient(object):
    __pool = None
    
    def __int__(self,**db_config):
        self.uuid = ''
        self.db_config = {}
        self.db = None
        self.digestdb = None
        
        self.start = datetime.strptime('2017-01-01', '%Y-%m-%d')
        self.end   = datetime.now()
        
    def __del__(self):
        if self.db is not None:
            self.db.close()
        if self.digestdb is not None:
            self.digestdb.close()
        if self.__pool is not None:
            self.__pool.close()
            
    def connectDB(self, **db_config):
        """
        @summary:
