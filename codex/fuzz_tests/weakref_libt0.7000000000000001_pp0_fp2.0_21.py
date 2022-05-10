import weakref
import logging

logger = logging.getLogger('MTWidget')

def _debug_log(func):
    def _func(self, *args, **kwargs):
        logger.debug("{}(self={}, args={}, kwargs={})".format(func.__name__, self, args, kwargs))
        value = func(self, *args, **kwargs)
        logger.debug("{}(self={}, args={}, kwargs={}) returned {}".format(func.__name__, self, args, kwargs, value))
        return value
    return _func

def _log(func):
    def _func(self, *args, **kwargs):
        logger.info("{}(self={}, args={}, kwargs={})".format(func.__name__, self, args, kwargs))
        value = func(self, *args, **kwargs)
        logger.info("{}(self={}, args={}, kwargs={}) returned {}".format(func.__name__, self, args, k
