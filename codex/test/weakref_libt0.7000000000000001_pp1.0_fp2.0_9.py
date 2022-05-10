import weakref

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.properties import (
    BooleanProperty,
    ListProperty,
    ObjectProperty,
    StringProperty,
)

from utils import memoize, get_all_subclasses


class TextInputRow(BoxLayout):
    '''Custom widget for text input.
    '''

    value = StringProperty('')
    '''String property to hold the value of the text input.
    '''

    label = StringProperty('')
    '''String property to hold the label text.
    '''

    text_input = ObjectProperty(None)
    '''Object property to reference the TextInput object.
    '''

    hide_clear_button = BooleanProperty(False)
    '''Boolean property to show/hide the clear button.
    '''
