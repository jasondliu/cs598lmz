import threading
# Test threading daemon, does not work with the main loop
# class Threaded(threading.Thread):
#     def __init__(self, target, *args):
#         self._target = target
#         self._args = args
#         threading.Thread.__init__(self)
#
#     def run(self):
#         self._target(*self._args)

# def from_thread(fn):
#     def run(*k, **kw):
#         t = Threaded(target=fn, args=k, kwargs=kw)
#         t.start()
#     return run

def _get_file_name(file_name):
    """
    Get the file name from the path
    :param file_name: the file name
    :return: the file name
    """
    return file_name.split('/')[-1]

def _get_file_path(file_name):
    """
    Get the file path from the path
    :param file_name: the file name
    :return: the file path
    """
    return file_
