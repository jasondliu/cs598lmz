import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

class AutocompleteEdit(ahkpy.object_):
    builtin_text = ahkpy.string_()
    dropDownList = ahkpy.string_()
    object_keys = ahkpy.string_()
    options = ahkpy.string_()
    sort = ahkpy.string_()
    consider_whitespace = ahkpy.integer_()

    def get_text(self):
        return ahkpy.ahk.call('AutoCompleteGetText', self.builtin_text.value)

    def set_text(self, s):
        return ahkpy.ahk.call('AutoCompleteGetText', self.builtin_text.value, s)


class ToolTip(ahkpy.object_):
    id = ahkpy.integer_()
    error = ahkpy.integer_()


class Edit(Window):
    id = ahkpy.integer_()

    class style_(ahkpy.object
