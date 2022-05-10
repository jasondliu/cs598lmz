import ctypes
# Test ctypes.CField
# Todo: Not implemented yet
class class_with_cfield:
    number_of_students = 5
    def __init__(self, data, handle, student_id):
        self.data = data
        self.handle = handle
        self.student_id = student_id

# TODO: Checked, but fails ..
## CPyMarshal.WriteInt(data, student_id)
## CPyMarshal.WriteIntField(data, class_with_cfield, 'number_of_students')

# Todo: Not done yet
class class_with_cfunction:
    @staticmethod
    def cfun(s) :
        return str(s) + " is calling a C function"
    def __init__(self, data):
        self.data = data
# Todo: Not done yet
class class_with_cproperty:
    number_of_students = 5
    def __init__(self, data, student_id):
        self.data = data
        self.student_id = student_id

    @property
   
