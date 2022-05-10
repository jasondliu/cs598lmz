import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)

DATA_PATH = "<Path to the data file>"

# create numpy ndarray
a = np.eread_csv(DATA_PATH)

def callback()
    # do something with the ndarray

timer = QTimer()
timer.start(1000)
callback = FUNTYPE(Callback)
timer.timeout.connect(callback)

app.exec()
</code>
and run the script with python.
I read about the FUNTYPE which is the only possibility to get a function as input in the connect function to the signal. My problem is that I am not able to call a function which is a class method. So I guess I have to make the function a "global" one and call it. Unfortunately I have to access my ndarray as a member variable in the callback function.
I tried to create a QObject and connected the signal with the funtype callback. 
How do I pass my ndarray to the callback function?
Or is there a better way to make the ndarray available in the class which implements the timer slots.
I am using PySide Qt 4.8
