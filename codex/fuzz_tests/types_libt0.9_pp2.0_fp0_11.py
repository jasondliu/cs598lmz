import types
types.ModuleType('mpl_toolkits')._path_.append('.')
%matplotlib inline

# Imports for the toolbox
import numpy as np
import vtk

# Imports our classes
from pyviz3d import renderwindow, surface, viewport
# Initialise a renderwindow
win = renderwindow()

# Load in sample VTK data
reader = vtk.vtkStructuredPointsReader()
reader.SetFileName('data/hydrogen.vtk')

# We want smooth normals
surface_filter1 = vtk.vtkSmoothPolyDataFilter()
surface_filter1.SetInputConnection(reader.GetOutputPort())
surface_filter1.SetNumberOfIterations(10)
surface_filter1.Update()

# Set it to a continuous greyscale
surf = surface(surface_filter1.GetOutputPort())
surf.face("w")
surf.edge("#000000")

# Add it to the window
win.add(surf)

# Display the window
win.render()

# Initialise a renderwindow
