import types
# Test types.FunctionType
visitor = myVisitor()
for node in visitor.visit(ast_node):
    if node.__class__ == types.FunctionType:
        print node
        print node.__name__
        print node.__doc__
        print node.__dict__
        print node.im_func
        print node.im_func.func_code
        #print node.im_func.func_code.

# Test types.MethodType
for node in visitor.visit(ast_node):
    if node.__class__ == types.MethodType:
        print node
        print node.__name__
        print node.__doc__
        print node.__dict__
        print node.im_func
        print node.im_func.func_code
        #print node.im_func.func_code.co_code
        #print node.im_func.func_code.co_consts
        #print node.im_func.func_code.co_names
        #print node.im_func.func_code.co_varnames
        #print
