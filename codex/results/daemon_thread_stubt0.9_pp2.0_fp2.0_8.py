import sys, threading

def run():
    os.chdir(dirname)

    print(os.getcwd())
    # Set the animation disable to False before showing the splash screen,
    # otherwise loading of the GUI could be reset and the form
    # is shown out-of-sync with the rest of the GUI.
    if QtCore.PYQT_VERSION_STR < '4.8.0':
        QtGui.QSplashScreen.setAnimationEnabled(False)

    # Install a custom ProgressBar for splash screen.
    splash = RnaMakerLauncher.SplashScreen()
    splash.show()
    splash.raise_()

    if QtCore.PYQT_VERSION_STR < '4.8.0':
        splash.showMessage("Starting ... Please wait", alignment=QtCore.Qt.AlignBottom)
    else:
        splash.showMessage("Starting ... Please wait", alignment=QtCore.Qt.AlignBottom, color=QtCore.Qt.darkGreen)

    qApp.processEvents()

    # Configure the environment before creating the main window.
    app
