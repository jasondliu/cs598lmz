import gc, weakref
import vtk

from vtk.util import numpy_support

# For display of images
import matplotlib.pyplot as plt

# Get the path to the directory with the files that we need
dataDir = os.path.dirname(os.path.realpath(__file__))

# Get the path to the STL file of the head
headFilePath = os.path.join(dataDir, "head.stl")

# Get the path to the vtk image data file
vtkImageFilePath = os.path.join(dataDir, "cthead1.vtk")

# Get the path to the vtk structured points file
vtkStructuredPointsFilePath = os.path.join(dataDir, "cthead1.vtk")

# Get the path to the vtk structured grid file
vtkStructuredGridFilePath = os.path.join(dataDir, "cthead1.vtk")

# Get the paths to the vtk rectilinear grid file
vtkRectilinearGridFilePath = os.path.join(dataDir,
