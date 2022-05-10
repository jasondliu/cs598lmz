import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# https://www.sqlite.org/c3ref/open.html

# int sqlite3_open(
#   const char *filename,   /* Database filename (UTF-8) */
#   sqlite3 **ppDb          /* OUT: SQLite db handle */
# );

# int sqlite3_open_v2(
#   const char *filename,   /* Database filename (UTF-8) */
#   sqlite3 **ppDb,         /* OUT: SQLite db handle */
#   int flags,              /* Flags */
#   const char *zVfs        /* Name of VFS module to use */
# );

# int sqlite3_close(sqlite3*);

# int sqlite3_close_v2(sqlite3*);

# int sqlite3_exec(
#   sqlite3*,                                  /* An open database */
#   const char *sql,                           /* SQL to be evaluated */
#   int (*callback)(void*,int,char**,char**),  /* Callback function */
#   void *,                                   
