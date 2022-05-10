import weakref
import json

reload(sys)
sys.setdefaultencoding("utf-8")

application = Bottle()

# Connect to Redis
redis = Redis()

# Handling JSON requests
def json_dumper(obj):
    try:
        return obj.to_json()
    except:
        return obj.__dict__

def hookjson():
    def hookjson(callback):
        def wrapper(*a, **ka):
            return json.dumps(callback(*a, **ka), default=json_dumper, sort_keys=True)
        return wrapper
    return hookjson

application.install(hookjson())

class RedisHash(object):
    _namespace = None
    _redis = None
    _fields = []

    def __init__(self, **kwargs):
        self._values = {}
        for field in self._fields:
            value = kwargs.get(field)
            if value is not None:
                self._set_value(field, value)
    
    @classmethod
    def _get_
