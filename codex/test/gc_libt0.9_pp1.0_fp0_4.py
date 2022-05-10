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
