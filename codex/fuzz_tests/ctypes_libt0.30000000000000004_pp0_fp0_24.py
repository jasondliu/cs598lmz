import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# Create the GUI application
app = wx.App()

# Create the main window and insert the custom frame
frame = MainFrame(None, "Hello World")
frame.Show()

# Run the application
app.MainLoop()
</code>

