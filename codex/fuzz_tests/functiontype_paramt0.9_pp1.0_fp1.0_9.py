from types import FunctionType
list(FunctionType(t.function,t.__globals__)() for t in th_list)
print(td_list[0].__globals__)

# =============================================================================
# using 
# =============================================================================
'''for i in range(10):
    t = test6()
    t.start()'''
