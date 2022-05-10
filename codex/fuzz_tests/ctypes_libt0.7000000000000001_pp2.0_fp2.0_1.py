import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# Reading input from GUI elements
if task.cb_1.isChecked():
    var_1 = task.cb_1.text()
elif task.cb_2.isChecked():
    var_1 = task.cb_2.text()
else:
    var_1 = task.cb_3.text()
# Open a file dialog
filename = QtWidgets.QFileDialog.getOpenFileName(task, 'Open File', 'c:\\', "Image files (*.jpg *.gif)")
filename = str(filename[0])

# Open a directory dialog
directory = QtWidgets.QFileDialog.getExistingDirectory(task, 'Open Directory', 'c:\\')
directory = str(directory)

# Creating a new window
new_task = Tasks.Task_2()
new_task.show()

# Closing a window
task.close()

# Adding a new tab to the tab widget
tabWidget_1 = task.TW_1

