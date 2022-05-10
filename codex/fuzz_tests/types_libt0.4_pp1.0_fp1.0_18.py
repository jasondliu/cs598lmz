import types
types.MethodType(lambda self: self.foo, obj)

#@-node:ekr.20040930105036.1:<< define the lambda function >>
#@nl

#@+others
#@+node:ekr.20041005105605.100:class leoTkinterFrame
class leoTkinterFrame (leoFrame.leoFrame):

    """A class that represents a Leo window."""

    #@    @+others
    #@+node:ekr.20041005105605.101:Birth & death
    #@+node:ekr.20041005105605.102:tkFrame.__init__
    def __init__ (self,c,parentFrame):

        # Init the base class.
        leoFrame.leoFrame.__init__(self,c,parentFrame)

        # g.trace("leoTkinterFrame",g.callers())

        self.createOutlineWidget()
        self.createIconBar()
        self.createComponent("body")
        self.createLog()
        self.create
