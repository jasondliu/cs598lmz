import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('datafile.db')

# Test for board lay-out
# Test for position
# Test for move to calclculation

# Test for version
# Test for data in tupple
# Test for display data on board

# Test for capture
# Test for display on board

# Test for AI (position strength, etc...)

# Test for Multiplayer (sockets, etc...)




class main():
    
    lib_book = LoadLibrary(ctypes.util.find_library('book'))

    #from book import Book

    book = lib_book.new_Book()
    lib_book.Book_size(book)

    #print p.value

    #lib_book.Book_size.argtypes = [Book]
    #lib_book.Book_size.restype   = c_int

    #from moveit import *

    libmoveit = LoadLibrary(ctypes.util.find_library('moveit'))
    
    #from moveit import *

    #from board import *

    libboard = LoadLibrary(ctypes.util.find_library('
