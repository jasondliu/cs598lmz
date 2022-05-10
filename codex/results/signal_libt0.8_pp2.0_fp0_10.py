import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a new window
window = sg.Window('Window Title', default_element_size=(40, 1), auto_size_text=False, auto_size_buttons=False)

layout = [[sg.Text('All graphic widgets in one window!', size=(40, 1))],
          [sg.Text('Here is some text.... and a place to enter text')],
          [sg.InputText('This is my text')],
          [sg.Frame(layout=[
             [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],
             [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
          [sg.Multiline(default_
