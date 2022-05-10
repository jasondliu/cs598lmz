import ctypes
ctypes.cast(0, ctypes.c_void_p)

ErrorMessage = "list index out of range"

def eval_loop():

    while True:
        try:
            print(eval(input("Input Python statement:")))
        except:
            print(ErrorMessage)
        while True:
            try:
                yes_or_no = input("continue? (y/n)")
                yes_or_no = str(yes_or_no)
                if "y" in yes_or_no:
                    break
                elif "n" in yes_or_no:
                    return
                else:
                    print("invalid input!")
            except:
                print(ErrorMessage)

eval_loop()
