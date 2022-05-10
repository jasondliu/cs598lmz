import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise Exception("Hello")

fun()

fm = FileManager()
fm.load_file("./test.pdf")
fm.save_file("./out.pdf")
fm.delete_file("./test.pdf")
fm.delete_file("./out.pdf")
fm.load_file("./test.pdf")
fm.save_file("./out.pdf")
fm.save_file("./out1.pdf")
fm.merge_file("./out.pdf","./out1.pdf","./out2.pdf")
fm.save_file("./out2.pdf")
fm.delete_file("./out.pdf")
fm.delete_file("./out1.pdf")
fm.delete_file("./out2.pdf")
fm.save_file("./out2.pdf")
fm.delete_file("./test.pdf")
fm.delete_file("./out2.pdf")

fm.save_file("./out2.pdf")
