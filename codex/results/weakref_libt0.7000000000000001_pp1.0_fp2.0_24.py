import weakref

from . import base
from . import resources


@base.returns_native_string
def _(message):
    return message


class PygletTranslator(resources.Translator):
    def _init(self):
        self._pyglet_translator = _pyglet_translator

    def gettext(self, message):
        return self._pyglet_translator.ugettext(message)

    def ngettext(self, message, plural_message, count):
        return self._pyglet_translator.ungettext(message, plural_message, count)


class PygletTextProvider(resources.TextProvider):
    def _init(self):
        self._pyglet_text_provider = _pyglet_text_provider

    def get_text(self, identifier, default):
        return self._pyglet_text_provider.get(identifier, default)


def init(localedir=None, translations=None, text_provider=None):
    global _pyglet_translator, _pyg
