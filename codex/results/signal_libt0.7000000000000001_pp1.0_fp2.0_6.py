import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class TestFileDialog(unittest.TestCase):
    def test_open_file_dialog(self):
        ''' 打开文件选择器 '''
        file_dialog_window = FileDialogWindow()
        file_dialog_window.show_and_focus()
        self.assertTrue(file_dialog_window.has_focus())

        open_file_dialog_button = file_dialog_window.child(roleName='push button', name='Open File Dialog')
        open_file_dialog_button.click()
        self.assertTrue(open_file_dialog_button.is_enabled())

        message_box_window = file_dialog_window.child(roleName='frame', name='Open File')
        self.assertTrue(message_box_window.has_focus())

        open_file_dialog_button = message_box_window.child(roleName='push button', name='打
