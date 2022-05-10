from types import FunctionType
list(FunctionType(a))
'''
        expect_output = '''[]'''
        self.assertTrue(TestCodeGen.test(input,expect_output,601))

    def test_func_call_without_return(self):
        input = """
def foo():
    a = 2
    b = 3
    a = func(a,b)[0][0]
    

def func(a, b):
    arr = []
    arr.append([a,b])
    return arr
foo()

"""
        expect_output = ""
        self.assertTrue(TestCodeGen.test(input,expect_output,602))

    
    def test_func_call_without_return_2(self):
        input = """
def foo():
    return 2
    a = 4
    bar(a)

def bar(a):
    a = 3

foo()

"""
        expect_output = ""
        self.assertTrue(TestCodeGen.test(input,expect_output,603))
    
    def test_return(self):
       
