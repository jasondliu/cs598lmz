import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char()

s = S()

if __name__ == "__main__":
    import support
    support.compileJPythonc("test380j.py", jar="test380.jar", core=1)
    support.runJava("-jar", "test380.jar", status=1)
    support.runJava("-jar", "test380.jar", status=1)
