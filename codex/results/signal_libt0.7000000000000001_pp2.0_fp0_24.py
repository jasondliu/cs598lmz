import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Define the editor object we're going to use.
if len(sys.argv) > 1:
    editor_object = sys.argv[1]
else:
    editor_object = 'editor'

# We want the editor to be able to see the application.
sys.path.append('..')

# Import the module we're going to use.
print('Importing %s...' % editor_object)
editor = __import__(editor_object)

# Launch the editor.
print('Launching %s...' % editor_object)
editor.launch()
