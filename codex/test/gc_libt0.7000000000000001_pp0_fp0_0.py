import gc, weakref
import sys, traceback

import logging

logger = logging.getLogger("fate.facade")

#------------------------------------------------------------------------------
# FATE
class FATE:
    def __init__(self, ptr):
        self.__wrapper = weakref.ref(ptr, self.__dealloc)
        self.__dealloc_func = None
        self.__dealloc_args = None

    def __dealloc(self, *args):
        if self.__dealloc_func:
            try:
                self.__dealloc_func(*self.__dealloc_args)
            except:
                logger.exception("FATE dealloc callback failed.")
        else:
            logger.debug("FATE dealloc callback not set.")

    def set_dealloc(self, func, *args):
        self.__dealloc_func = func
        self.__dealloc_args = args

    def get_ptr(self):
        return self.__wrapper()

#------------------------------------------------------------------------------
# PythonFacade
