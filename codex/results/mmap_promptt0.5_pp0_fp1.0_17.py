import mmap
# Test mmap.mmap(0, 1, "MMAP", mmap.MAP_SHARED, os.open("/dev/zero", os.O_RDONLY))

# This is the main entry point for the module.
# It loads the main class and starts the application.
def run():
    # Create the main application window
    app = wx.App()
    # Create the main frame
    frame = MainFrame()
    # Show the frame
    frame.Show()
    # Start the event loop
    app.MainLoop()

# Run the module
if __name__ == "__main__":
    run()
