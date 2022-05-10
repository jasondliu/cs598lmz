import types
# Test types.FunctionType
def my_equiv_comp(obj1, obj2):
	if type(obj1) == types.FunctionType:
		if (obj1.func_code.co_code == obj2.func_code.co_code or
		len(obj1.func_code.co_code) == len(obj2.func_code.co_code)):
			return True
		return False
# Original my_equiv_comp
# def my_equiv_comp(obj1, obj2):
# 	if type(obj1) == int or type(obj1) == float:
# 		if (obj1 == obj2 or 
# 			len(obj1) == len(obj2)):
# 			return True
# 		return False
# 	if type(obj1) == str:
# 		if (obj1 == obj2 or 
# 			len(obj1) == len(obj2)):
# 			return True
# 		return False
# 	
