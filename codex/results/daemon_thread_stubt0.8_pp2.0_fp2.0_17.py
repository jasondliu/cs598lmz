import sys, threading

def run():
    app = QtWidgets.QApplication(sys.argv)
    progress_bar = ProgressBar()
    progress_bar.show()
    sys.exit(app.exec_())

def update():
    global progress_bar
    for i in range(10, 100, 10):
        print("%i%%" % i)
        progress_bar.setValue(i)
        sleep(1)


t = threading.Thread(target=update)
t.start()
run()
</code>

