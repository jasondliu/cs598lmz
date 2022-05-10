import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')

from pypy.rpython.lltypesystem import lltype, rffi
from pypy.translator.tool.cbuild import ExternalCompilationInfo

# ____________________________________________________________

class CConfig:
    _compilation_info_ = ExternalCompilationInfo(
        includes = ['stdio.h', 'dlfcn.h'],
        separate_module_sources = ['''
            void* dlopen(const char* path, int mode);
            void* dlsym(void* handle, const char* symbol);
            int dlclose(void* handle);
            void* dlerror(void);
        ''', '''
            #ifdef _WIN32
            #define RTLD_LAZY 0
            #define RTLD_NOW 0
            #define RTLD_GLOBAL 0
            #define RTLD_LOCAL 0
            #define RTLD_NODELETE 0
            #define RTLD_NOLOAD 0
            void* dlopen(const char* path, int mode) {return
