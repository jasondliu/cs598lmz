from types import FunctionType
a = (x for x in [1])
print(type(a))
def a():pass
print(type(a))
print(isinstance(a,FunctionType))
print(float('nan'))
from flask.json import JSONEncoder
import datetime,time
from flask import jsonify
from flask import make_response
a = datetime.datetime.fromtimestamp(time.time())
b = 'string'
from flask.json import JSONEncoder
import datetime
from flask import jsonify
from flask import make_response

class JSONEncode(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,datetime.datetime):
            return 'a'
        else:
            return super().default(obj)

b = JSONEncode().encode({'a':'b','b':a})
print(b)
#data = jsonify({"a":a,"b":b})
#data = JSONEncode().encode({'a':'b','b':b})
#data = make_response(a)
#print(type(data.data))
print(b
