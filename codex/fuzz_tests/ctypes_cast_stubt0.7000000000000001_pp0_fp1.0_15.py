import ctypes
ctypes.cast(0, ctypes.py_object)

import llvmpy

def main():
    """
    A simple example demonstrating how to setup an optimizer and codegen
    object, and then run an optimization pass over some LLVM IR.
    """
    # initialize LLVM
    llvmpy.initialize()
    llvmpy.initialize_native_target()

    # create some LLVM types
    void_ty = llvmpy.core.Type.void()
    fnty = llvmpy.core.Type.function(void_ty, [void_ty])

    # setup our builder, module, and function
    module = llvmpy.core.Module.new('my_module')
    function = llvmpy.core.Function.new(module, fnty, 'my_function')
    block = function.append_basic_block('entry')
    builder = llvmpy.core.Builder.new(block)

    # create a ret void instruction
    builder.ret_void()

    # create a target machine and codegen object
   
