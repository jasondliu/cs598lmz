import ctypes
ctypes.cast(id(self), ctypes.py_object).value

# To do:
# 1. Add a drop down list for all paths to choose from
# 2. Add a drop down list for all file names to choose from
# 3. Add a drop down list for all sheet names to choose from
# 4. Add a drop down list for all column names to choose from
# 5. Add a button to run the code

# Create the application window
root = Tk()
root.title("Excel Read")
root.geometry("800x300")

# Create a label and text entry box for the path
path_label = Label(root, text="Path:")
path_label.grid(row=0, column=0, sticky=W)
path_entry = Entry(root, width=80)
path_entry.grid(row=0, column=1, sticky=W)

# Create a label and text entry box for the file name
file_label = Label(root, text="File Name:")
file_label.grid(row=1, column=0, sticky=W)
file_entry =
