import ctypes
# Test ctypes.CFUNCTYPE.

if __name__ == "__main__":
    import sys
    import support
    support.compileJPythonc("test156c.java", output="test156.err",
            javaProperties="-Dpython.home=" + sys.prefix)
    support.runJava("test156c", classpath="jpywork")
