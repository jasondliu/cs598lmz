import ctypes
import ctypes.util
import threading
import sqlite3

from . import lmdb_cffi

_ffi = ctypes.FFI()

_ffi.cdef('''
typedef int mdb_mode_t;
typedef int mdb_filehandle_t;
typedef unsigned int size_t;
typedef int mdb_dbi_t;

typedef ... MDB_env;
typedef ... MDB_txn;
typedef ... MDB_cursor;
typedef ... MDB_val;

typedef struct MDB_envinfo {
    size_t me_mapsize;
    size_t me_last_pgno;
    size_t me_last_txnid;
    unsigned int me_maxreaders;
    unsigned int me_numreaders;
} MDB_envinfo;

typedef struct MDB_stat {
    size_t ms_psize;
    size_t ms_depth;
    size_t ms_branch_pages;
    size_t ms_leaf_pages
