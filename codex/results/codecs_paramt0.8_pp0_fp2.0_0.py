import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _stringify(value):
    if isinstance(value, six.binary_type):
        return value.decode('utf-8', 'strict')
    elif isinstance(value, six.string_types):
        return value
    else:
        return str(value)

class BaseJsonEncoder(json.JSONEncoder):
    """
    An encoder that serializes datetime and UUID to string, without
    serializing `content_object` field. 
    """
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif isinstance(obj, uuid.UUID) :  # pragma: no cover
            return str(obj)
        else:
            try:
                return super(BaseJsonEncoder, self).default(obj)
            except TypeError:  # pragma: no cover
                return str(obj)

def _make_response(value, status, headers=None):
    """
   
