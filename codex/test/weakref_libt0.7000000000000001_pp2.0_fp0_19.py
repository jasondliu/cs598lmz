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

