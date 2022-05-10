import ctypes
ctypes.cast(0, ctypes.py_object)

def main():
    env = Environment()

    ast = parse_file(
        '../examples/input_output_functions/input_output_functions.txt',
        env
    )
    ast.eval()


    ast = parse_file(
        '../examples/input_output_functions/input_output_functions2.txt',
        env
    )
    ast.eval()


