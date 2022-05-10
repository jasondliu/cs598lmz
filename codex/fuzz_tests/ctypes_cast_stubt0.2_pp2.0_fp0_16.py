import ctypes
ctypes.cast(0, ctypes.py_object).value

# 파이썬 객체를 바이트 문자열로 변환하기
import pickle
pickled = pickle.dumps(obj)

# 바이트 문자열을 파이썬 객체로 변환하기
obj = pickle.loads(pickled)

# 파이썬 객체를 파일에 쓰기
f = open('somefile', 'wb')
pickle.dump(obj, f)
f.close()

# 파일에서 파이썬 객체 읽기
f = open('somefile', 'rb')
obj
