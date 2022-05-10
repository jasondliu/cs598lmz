import types
# Test types.FunctionType
def is_function(input_function,input_string):
   if type(input_function)==types.FunctionType:
       return input_function(input_string)
   else:
       print("Incorrect input of function")
# Test sum_list()
def sum_list(input_list):
    if type(input_list)==list:
        return sum([int(i) for elem in input_list for i in elem])
    else:
        print("Incorrect input of list")
# Test same_type()
def same_type(*input_types):
    if all([type(i)==input_types[0] for i in input_types]):
        return True
    else:
        return False
        
# Test elements_with_same_keys()
def elements_with_same_keys(input_dict):
    if type(input_dict)==dict:
        values=[list(i.values()) for i in input_dict.values()]
        dict_key=list(input_dict.keys())
        new_dict={key:values for
