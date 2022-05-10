from types import FunctionType
a = (x for x in [1])
print(isinstance(a,GeneratorType))
print(isinstance(a,FunctionType))
print(isinstance(a,list))
print(isinstance(a,str))
print(isinstance(a,object))

print(isinstance(None,object))
print(isinstance(None,str))
print(isinstance(None,list))

# 异常捕获
import time
time.sleep(2)
try:
    print("try")
except Exception:
    print("except")
else:
    print("else")
finally:
    print("finally")

# 遍历文件夹
import os
def traverse_dir(path):
    for file in os.listdir(path):
        file_path = path + '/' + file
        if os.path.isdir(file_path):
            traverse_dir(file_path)
        else:
            print(file_path)

path = r'D:\python_work\python_code'
traverse_dir(path
