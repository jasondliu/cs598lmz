import threading
threading.stack_size(1024 * 1024 * 32)  # Increase stack size of the thread

# Run the app
app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
