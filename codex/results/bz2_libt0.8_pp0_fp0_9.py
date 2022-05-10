import bz2
bz2_serializer = pickle_serializer.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
pickle.loads(bz2_serializer)

#msgpack (msgpack.org)
import msgpack
msgpack_serializer = msgpack.dumps(obj)
msgpack.loads(msgpack_serializer)

#JSON (JSON.org)
import json
json_serializer = json.dumps(obj, default=json_serializer, ensure_ascii=False)
json.loads(json_serializer)
def json_serializer(obj):
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    elif isinstance(obj, timedelta):
        return (datetime.min + obj).time().isoformat()

#Joblib
import joblib
joblib_serializer = joblib.dumps(obj)
joblib.loads(joblib_serializer)

#JSON with numpy and pandas
import json
import numpy as np
import pandas as
