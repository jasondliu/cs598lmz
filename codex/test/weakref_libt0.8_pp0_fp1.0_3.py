import weakref

import Cocoa
import objc

from defconAppKit.objects.font import DefconAppKitFont
from defconAppKit.tools.textSplitter import splitText
from defcon.objects.base import BaseObject
from defcon.objects.defcon import RGlyph
from defcon.objects.defcon import Font
from defconAppKit.widgets.progressController import ProgressController
from defconAppKit.windows.baseWindow import BaseWindowController


class GlyphsPaletteBaseObject(BaseObject):

    def __init__(self, font):
        super(GlyphsPaletteBaseObject, self).__init__()
        self.font = font


class GlyphsPaletteFont(DefconAppKitFont):

    def __init__(self, path, glyphOrder=None):
        if glyphOrder is None:
            glyphOrder = []
        super(GlyphsPaletteFont, self).__init__(path)
        self.glyphOrder = glyphOrder


