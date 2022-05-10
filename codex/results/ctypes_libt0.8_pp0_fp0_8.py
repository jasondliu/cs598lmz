import ctypes
ctypes.windll.user32.MessageBoxW(0, "Python says hello", "Hello", 1)
 

def fun1(name):
    print("hello",name)

fun1("python")
fun1("java")
