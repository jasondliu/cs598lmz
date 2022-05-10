import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Load the KV language rules:
Builder.load_file('main.kv')

class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()
