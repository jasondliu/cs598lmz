import threading
threading.currentThread().setName("MainThread")

# import the MainWindow widget from the converted .ui files
from ui.mainwindow import Ui_MainWindow

# import the other windows
from ui.windows.window_new_project import WindowNewProject
from ui.windows.window_edit_project import WindowEditProject
from ui.windows.window_delete_project import WindowDeleteProject
from ui.windows.window_new_task import WindowNewTask
from ui.windows.window_edit_task import WindowEditTask
from ui.windows.window_delete_task import WindowDeleteTask
from ui.windows.window_add_employee import WindowAddEmployee
from ui.windows.window_edit_employee import WindowEditEmployee
from ui.windows.window_delete_employee import WindowDeleteEmployee
from ui.windows.window_add_timesheet import WindowAddTimesheet
from ui.windows.window_edit_timesheet import WindowEditTimesheet
from ui.windows.window_delete_timesheet import WindowDeleteTimesheet
