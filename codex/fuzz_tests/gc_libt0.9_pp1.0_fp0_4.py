import gc, weakref

class WeakSceneDict(weakref.WeakValueDictionary):
    def addScene(self, scene):
        self[scene.sceneID] = scene
    
    def add(self, key, ref):
        '''attr ref to our dict'''
        self[key] = ref

class WeakSet(set):
    def add(self, obj):
        '''Use a WeakRef to add an object to our set'''
        self.add( weakref.ref(obj) )

class Scene(object):
    """Raises an exception if an interface isn't implemented"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, sceneID, autoStart):
        '''
        sceneInitSettings -- a weakref to a collection of settings (if there are any needed)
        '''
        self.sceneID = sceneID
        self.autoStart = autoStart
        self.isActiveScene = False
        self._started = False
        self.staticObjects = WeakSet()
        self.dynamicObjects = WeakSceneDict()


