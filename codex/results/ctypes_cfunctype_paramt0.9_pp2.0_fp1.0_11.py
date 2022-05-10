import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
functionList = []

for i in range(1000):
    f = FUNTYPE(lambda: None)
    functionList.append(f)


# for i in range(2):
#     for item in functionList:
#         item()

# def wwrap(f):
#     def foo(*arg):
#         f()
#     return foo
# fun1 = wwrap(fun)
# for i in range(2):
#     for item in functionList:
#         item()
# functionList = [wwrap(f) for f in functionList]
# functionList = [f() for f in functionList]

# for i in range(2):
#     for item in functionList:
#         item()
