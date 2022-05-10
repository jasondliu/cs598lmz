import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# SINGLETON MODE
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# DECORATOR TO MULTIPROCESS
def multiprocess(function):
    def wrapper(*args, **kwargs):
        process = multiprocessing.Process(target=function, args=args, kwargs=kwargs)
        process.start()
        return process
    return wrapper

# DECORATOR TO AUTO-RUN
def autorun(function):
    def wrapper(*args, **kwargs):
        def run_it():
            function(*args, **kwargs)
        threading.Thread(target=run_it).start()
    return wrapper

# DECORATOR TO AUT
