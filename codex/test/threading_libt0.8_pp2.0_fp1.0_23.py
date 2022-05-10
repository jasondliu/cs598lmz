import threading
threading.Thread(target=evaluate, args=(1, 2), kwargs={'foo': 'bar'}).start()

class Evaluator:
    def __init__(self, db, name, verbose=False):
        self.name = name
        self.connected = False
        self.db = db
        self.db.add_evaluator(self)
        self.verbose = verbose

    def eval_function(self, func, args, kwargs):
        if self.verbose:
            print(self.name, "execute", func.__name__, args, kwargs)
        self.db.start_eval(self, func.__name__)
        ret = func(*args, **kwargs)
        self.db.end_eval(self, func.__name__)
        if self.verbose:
            print(self.name, "done", ret)
        return ret

class Database:
    def __init__(self, verbose=False):
        self.evaluators = []
        self.counter = 0
        self
