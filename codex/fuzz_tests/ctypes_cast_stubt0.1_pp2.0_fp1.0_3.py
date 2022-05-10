import ctypes
ctypes.cast(0, ctypes.py_object).value

# 파이썬 객체를 바이트로 변환하는 방법
import pickle
pickle.dumps(obj)

# 바이트를 파이썬 객체로 변환하는 방법
pickle.loads(pickled_bytes)

# 바이트를 파이썬 객체로 변환하는 방법
import json
json.loads(json_bytes)

# 파이썬 객체를 바이트로 변환하는 방법
json.dumps(obj)

