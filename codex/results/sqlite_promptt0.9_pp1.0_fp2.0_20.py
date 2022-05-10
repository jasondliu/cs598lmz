import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/Users/Yajie/Documents/programs/AOS/sin_fitting_data/aos_fav_test.db')

# This is data base class, using sqlite3
# Many tables have been designed
#            * aos_User_info
#            * aos_Case_record
#            * aos_DUT_record
#            * aos_Station_record
#            * aos_Parameter_record
#            * aos_Fav_test_record
#
#
#
#
#
#
#
#
#


# sqlite3 database operation helper class
        
class sqlite3_database():
    def __init__(self):
        self.db_name = None
        self.conn = None
        self.caselist = None
        self.wait_list = None
        self.threadlist = None
        self.cur = None
        self.__first_run = True
        pass
    
    def __del__(self):
        """
        call db.close()
        """
        self.close()
       
