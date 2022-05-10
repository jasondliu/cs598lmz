import gc, weakref

from .model import *
from .key import *
from .pipeline import *
from .util import *

def _get_model_key(model):
    key = weakref.ref(model)
    return key

class ModelNotFoundError(Exception):
    pass

class ModelNotConnectedError(Exception):
    pass

class ModelManager(object):
    def __init__(self):
        self._models = {}
        self._model_keys = {}
        self._model_pipelines = {}
        self._model_transforms = {}
        self._model_transform_keys = {}

    def add_model(self, model):
        key = _get_model_key(model)
        self._model_keys[key] = model
        self._model_pipelines[key] = {}
        self._model_transforms[key] = {}

    def get_model(self, key):
        return self._model_keys.get(key, None)

    def has_model(self, key):
        return key in self._model_
