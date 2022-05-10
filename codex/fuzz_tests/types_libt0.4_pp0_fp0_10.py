import types
types.FunctionType

# 객체를 직렬화하는 방법
# pickle 모듈을 사용
# pickle.dump(객체, 파일객체)
import pickle
f = open("test.obj", "wb")
obj = {1: "python", 2: "you need"}
pickle.dump(obj, f)
f.close()

# pickle.load(파일객체)
f = open("test.obj", "rb")
obj = pickle.load(f)
print(obj)
f.close()

# pickle 모듈은 파이썬에서만 사용할 수 있는 모듈이다.
# 다른 프로그
