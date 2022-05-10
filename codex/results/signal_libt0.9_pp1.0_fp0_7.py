import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def test_open_dialog_cancel(qtbot, image_file):
    app = QApplication([])
    widget = GTViewerPanel()
    widget.show()
    qtbot.addWidget(widget)

    widget.configuration["open_dialog"]["enable"] = "true"
    widget.configuration["open_dialog"]["save_last_directory"] = "true"
    widget.configuration["open_dialog"]["start_in_home"] = "false"
    widget.configuration["open_dialog"]["start_in_current"] = "false"
    widget.configuration["open_dialog"]["start_in_last_directory"] = "true"
    widget.configuration["open_dialog"]["last_directory"] = "tests"
    widget.configuration["open_dialog"]["directory"] = "."
    widget.configuration["open_dialog"]["filter"] = "Images only (*.
