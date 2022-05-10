import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("TeraCopy Bypass")

def bypass_teracopy():
    while True:
        #Prompt user input
        print("Type 'exit' to quit the program\n")
        user_input = input("Drag & drop a file into the terminal: ")
        if user_input == "exit":
            print("\nBye!")
            break
        else:
            #Try to copy the file and print the result
            try:
                shutil.copy(user_input, "C:\\")
                print("\nFile copied successfully!\n")
            except Exception as e:
                print("\nError:" + str(e) + "\n")

if __name__ == "__main__":
    bypass_teracopy()
