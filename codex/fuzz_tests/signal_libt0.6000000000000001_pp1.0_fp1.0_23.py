import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# import QT and VTK libraries
from PyQt4 import QtCore, QtGui
from vtk import *

# import UI
from ui.mainwindow import Ui_MainWindow
from ui.vtk_widget import QVTKRenderWindowInteractor

# import controller
from controller.controller import Controller

# import custom widgets
from widgets.parameter_editor import ParameterEditor
from widgets.parameter_label import ParameterLabel
from widgets.data_list_view import DataListView
from widgets.data_parameter_list import DataParameterList
from widgets.data_parameter_editor import DataParameterEditor
from widgets.data_parameter_label import DataParameterLabel
from widgets.pipeline_list import PipelineList
from widgets.multi_input_parameter_editor import MultiInputParameterEditor
from widgets.multi_input_parameter_label import MultiInputParameterLabel
from widgets.vtk_scene_view import VTKSceneView
from widgets.vtk_scene_list import VTKScene
