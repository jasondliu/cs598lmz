import select, sys, time
from pyutil.program.log import get_logger

class CmdHandler(object):

    class __impl(object):
        def __init__(self):
            self.__logger = get_logger()
            self.__watches = dict()

        def register(self, name, handler, timeout=0):
            if name in self.__watches:
                return False
            self.__watches[name] = (time.time(), handler, timeout)
            return True

        def run(self):
            while True: 
                try:
                    if self.__poll():
                        self.__timeout()
                except KeyboardInterrupt:
                    self.__logger.info('receive KeyboardInterrupt, quit')
                    return
                except Exception as e:
                    self.__logger.error(e)

        def __poll(self):
            r_list, w_list, x_list = select.select(self.__watches.values(), [], [])
            for fd, event in r_list:
                fd[1
