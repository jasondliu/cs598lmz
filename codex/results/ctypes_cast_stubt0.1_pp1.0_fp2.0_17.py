import ctypes
ctypes.cast(0, ctypes.py_object).value

# 파이썬 객체를 바이트로 변환하기
import pickle
pickled = pickle.dumps(42)
pickled

# 바이트를 파이썬 객체로 변환하기
pickle.loads(pickled)

# 파이썬 객체를 바이트로 변환하기
import json
json.dumps(42)

# 바이트를 파이썬 객체로 변환하기
json.loads('42')

# 파이썬 객체를
