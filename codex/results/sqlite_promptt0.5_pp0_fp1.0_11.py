import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

# This is the interface for the database
# The database is a sqlite3 database
# The table is called 'quotes'
# It has two columns, 'quote' and 'source'
# Both are TEXT

# The database is stored in the file 'quotes.db' in the current directory
# The database is created automatically if it doesn't exist

# The database is locked while a query is running
# Any other threads will wait until the lock is released

# The database provides the following methods:
#
# get_quote(self)
#   returns a random quote from the database
#
# get_quotes(self)
#   returns a list of all quotes
#
# add_quote(self, quote, source)
#   adds a quote to the database
#   returns True if the quote was added, False if it was not
#
# remove_quote(self, quote)
#   removes a quote from the database
#   returns True if the quote was removed, False if it was not
#
# close(self)
#   closes the database

# The database
