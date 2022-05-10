import types
types.MethodType(lambda self: self.set_value(self.get_value()),
                 gtk.SpinButton, gtk.SpinButton, "set_value")

# This is a workaround for the fact that the Gtk.Entry.set_text() method
# doesn't emit the "changed" signal.
gtk.Entry.set_text = types.MethodType(lambda self, text:
                                      gtk.Entry.do_changed(self),
                                      gtk.Entry, gtk.Entry, "set_text")

# This is a workaround for the fact that the Gtk.TreeView.set_model() method
# doesn't emit the "row-inserted" signal.
gtk.TreeView.set_model = types.MethodType(lambda self, model:
                                          gtk.TreeView.do_row_inserted(self,
                                                                       None,
                                                                       None,
                                                                       None),
                                          gtk.TreeView, gtk.TreeView,
                                          "set_model")

# This is a workaround
