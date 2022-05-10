import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

try:
    import _json
except (ImportError, AttributeError):
    try:
        import briefjson as _json  # try briefjson first, because simplejson is too slow
    except ImportError:
        try:
            import simplejson as _json
        except ImportError:
            import json as _json

# json module's dump/dumps have an ensure_ascii parameter.
# If ensure_ascii is false, the result may be a unicode instance.
# This does not work well with ftplib.
# So we have to make it work like ensure_ascii=True.

# override json.dump and json.dumps to automatically encode utf-8

def _dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
          allow_nan=True, cls=None, indent=None, separators=None,
          encoding='utf-8', default=None, sort_keys=False, **kw):
    if cls is None
