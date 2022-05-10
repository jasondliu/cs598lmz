import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

# Create a sample application to demonstrate the use of the class
if __name__ == "__main__":
    import time

    # Set up a sample application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Create a button widget to use for the progress bar
    btn = QPushButton('Test', None)
    btn.setFixedSize(100, 50)

    # Create the progress bar
    progress = ProgressBar()

    # Create a vertical box layout to hold the button and progress bar
    layout = QVBoxLayout()
    layout.addWidget(btn)
    layout.addWidget(progress)

    # Create a widget to display the layout
    widget = QWidget()
    widget.setLayout(layout)
    widget.show()

    # Connect the clicked signal to a slot
    btn.clicked.connect(progress.start)

    # Run the sample application
    sys.exit(app.exec_
