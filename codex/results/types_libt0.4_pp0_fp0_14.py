import types
types.ModuleType.__dict__['__getattr__'] = lambda self, name: self.__getattribute__(name)
types.ModuleType.__dict__['__setattr__'] = lambda self, name, value: self.__setattr__(name, value)

# from . import _pywrap_tensorflow
# from . import pywrap_tensorflow
# from . import tensorflow
# from . import tensorflow_estimator
# from . import tensorflow_hub
# from . import tensorflow_io
# from . import tensorflow_lite
# from . import tensorflow_serving
# from . import tensorflow_text

# from . import _pywrap_tensorflow_internal
# from . import pywrap_tensorflow_internal
# from . import tensorflow_internal

# from . import _pywrap_tensorflow_internal_api
# from . import pywrap_tensorflow_internal_api
# from . import tensorflow_internal_api

# from . import _pywrap_tensorflow_internal_api_
