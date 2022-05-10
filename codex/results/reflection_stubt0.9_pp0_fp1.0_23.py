fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

JSONDecoder().decode(json.dumps({"__module__": 1}))
"""
import simplejson

t = simplejson.loads('{"__module__": 1}')
t['__module__']
