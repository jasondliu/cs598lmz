import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
num = 6
FUNC_TEST = FUNTYPE(num)
print(FUNC_TEST)
print(FUNC_TEST.__code__.co_argcount)
print(FUNC_TEST(10))
print(FUNC_TEST(200))
ctypes.windll.kernel32.SetConsoleTitleW(u"Macrosoft")

if __name__=="__main__": main()
