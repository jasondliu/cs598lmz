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
