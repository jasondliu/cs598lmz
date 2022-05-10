import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("Aspex")

#import py_compile
#py_compile.compile("aspex.py")

class addPoint_list:
    def __init__(self, stop_mode, choice, input_python, key, value, point, file_mode, filename, file_name, indentation):
        self.stop_mode = stop_mode
        self.choice = choice
        self.input_python = input_python
        self.key = key
        self.value = value
        self.point = point
        self.file_mode = file_mode
        self.filename = filename
        self.file_name = file_name
        self.indentation = indentation

#Data to be used by pythons new() method
def python_new(data):
    new_dict = dict()
    for x in range(len(data)):
        append_new_dict(new_dict, data[x].key, data[x].value, data[x].point)
    return new_dict

def append_
