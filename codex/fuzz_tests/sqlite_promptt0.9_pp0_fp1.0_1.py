import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# sqlite_file = 'e:\pylib\db\people.db'    # name of the sqlite database file
# table_name1 = 'my_table_1'   # name of the table to be created
# table_name2 = 'my_table_2'   # name of the table to be created
# new_field = 'my_1st_column' # name of the column
# field_type = 'INTEGER'  # column data type


'''We run this a million times against our enemies if reset will not work'''
def kill_lcd_proc(procname):
    from subprocess import Popen, PIPE, STDOUT
    # call = "taskkill /F /im " + procname
    call = "taskkill /F /im python.exe /im LCDC.exe /im chromedriver.exe"
    process = Popen(call, stdin=PIPE,
                    stdout=PIPE, shell=True, stderr=STDOUT)  # Open a  thread

    (output, err) = process.communicate
