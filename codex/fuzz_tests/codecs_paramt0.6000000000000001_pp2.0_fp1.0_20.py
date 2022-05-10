import codecs
codecs.register_error('arepl-replace', AreplReplace)

class Arepl(sublime_plugin.TextCommand):

    def run(self, edit):

        view = self.view
        sel = view.sel()
        sel_region = sel[0]
        region = sublime.Region(0, view.size())

        code = view.substr(region)

        if code is None:
            return

        self.save_pos()
        self.clear_selection()

        self.setup_repl()

        # start the REPL
        self.repl.start()

        # send the code to the REPL
        self.repl.send(code)

        # send a EOF to the REPL, stop it
        self.repl.send(chr(4))
        self.repl.stop()

        self.restore()

        # self.view.run_command("revert")

    def setup_repl(self):
        """
        Setup the REPL
        """
        self.repl = REPL.REPL(self)

    def save_pos(self):
        """
       
