import ctypes
ctypes.cast(0, ctypes.py_object)

# importing this module allows the automatic registration of our plugin
# with VisIt.
import visit

# Create a plugin that is not visible
#visit.PluginManager.Initialize()

# Open the database
#visit.OpenDatabase("/Users/kowalski/Documents/Work/Data/vis_data/plt00005")

# Add the plot
#visit.AddPlot("Contour", "density")

# Draw the plot
#visit.DrawPlots()

# Save the image
#visit.SaveWindow()

# Connect to VisIt
visit.Connect("localhost", 22222)

# Open the database
visit.OpenDatabase("/Users/kowalski/Documents/Work/Data/vis_data/plt00005")

# Add the plot
visit.AddPlot("Contour", "density")

# Draw the plot
visit.DrawPlots()

# Save the image
visit.SaveWindow()
