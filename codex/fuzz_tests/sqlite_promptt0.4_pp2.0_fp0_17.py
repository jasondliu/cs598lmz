import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# http://www.sqlite.org/c3ref/open.html
# int sqlite3_open(
#   const char *filename,   /* Database filename (UTF-8) */
#   sqlite3 **ppDb          /* OUT: SQLite db handle */
# );
# int sqlite3_close(sqlite3*);
# int sqlite3_exec(
#   sqlite3*,                                  /* An open database */
#   const char *sql,                           /* SQL to be evaluated */
#   int (*callback)(void*,int,char**,char**),  /* Callback function */
#   void *,                                    /* 1st argument to callback */
#   char **errmsg                              /* Error msg written here */
# );

# http://www.sqlite.org/c3ref/busy_timeout.html
# int sqlite3_busy_timeout(sqlite3*, int ms);

# http://www.sqlite.org/c3ref/busy_handler.html
# int sqlite3_busy_handler(sqlite3
