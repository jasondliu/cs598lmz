import gc, weakref

from pyglet.gl import *
from pyglet import image
from pyglet.window import key

from pyglet.text import document, layout, caret, style, util, formatter
from pyglet.text.layout import Control, Label, Caret, Selection, Layout


class DebugLayout(Layout):
    '''Layout that prints the document to stdout.
    '''
    def __init__(self, document, width, **kwargs):
        super(DebugLayout, self).__init__(document, width, **kwargs)
        self.labels = []

    def create_fragment(self, document, start, end):
        '''Create a fragment of the document.

        :Parameters:
            `document` : `document.AbstractDocument`
                Document to create the fragment from.
            `start` : int
                First character position of the fragment in the document.
            `end` : int
                Last character position of the fragment in the document.
        '''
        #print 'create_fragment', start, end
        fragment = document.
