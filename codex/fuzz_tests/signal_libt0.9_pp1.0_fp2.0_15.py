import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#import main script
import main_window_rt3_ui 

##
# Python "reload" for easier developing
##
finished = False
def reload_main():
    global finished
    finished = True
    if app:
        app.quit()
    print('reloading...')
    global app, ui
    app = QtWidgets.QApplication(sys.argv) 
    app.setApplicationName('Goat Plotter: Real Time Demo')
    ui = main_window_rt3_ui.Ui_MainWindow()
    ui.setupUi(ui)
    ui.pushButton.clicked.connect(reload_main)
    sys.exit(app.exec_())

##
# Main call
##
if not finished: reload_main()
