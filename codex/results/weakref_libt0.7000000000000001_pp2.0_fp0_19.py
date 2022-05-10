import weakref

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MMCorePy:
    def __init__(self):
        self.mmc = MMCorePy_wrap()

    def __del__(self):
        print 'del'
        self.mmc = None

    def __getattr__(self, name):
        return getattr(self.mmc, name)

# The following is only used for debugging purposes.
mmc = MMCorePy()

class MMCorePy_wrap(object):
    def __init__(self):
        self.instance = MMCorePy_wrap.MMCorePy_wrap_instance()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    class MMCorePy_wrap_instance(object):
        def __init__(self):
            try:
                self._
