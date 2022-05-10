import codecs
codecs.register_error("strict", codecs.ignore_errors)

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

def json_encode(obj):
    return JSONEncoder().encode(obj)

def json_decode(obj):
    return json.loads(obj)

def json_decode_with(obj, encoding):
    return json.loads(obj.decode(encoding))

def json_encode_with(obj, encoding):
    return JSONEncoder().encode(obj).encode(encoding)

def json_encode_iso(obj):
    return json_encode(obj).replace("T", " ").replace("Z", "").replace("+00:00", "")

class JSONEncoderWithEncoding(JSONEncoder):
    def __init__(self, encoding):
        JSONEncoder.__init__(self)
        self
