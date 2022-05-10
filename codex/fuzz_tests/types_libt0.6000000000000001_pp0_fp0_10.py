import types
types.ModuleType

# This class is the main entry point for your application.
# It loads the main.kv file, which has a reference to your root widget.
# This class can be accessed anywhere inside the kivy app as, for example:
#     from main import MainApp
class MainApp(App):
    def build(self):
        return root

    def on_start(self):
        self.root.ids.screen_manager.current = 'menu'


# Run the class and show the Kivy app
if __name__ == '__main__':
    MainApp().run()
