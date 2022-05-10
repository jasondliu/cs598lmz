import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Colormap(tpg.CompositeNode):
    r"""
    Class which produces color map.

    Parameters
    -----------
    domain : array_like
        Domain of the colorbar.
    number_colors : int
        Number of colors to use in the color map.
    static_colors : array_like
        List of colors that cannot be changed.
    """

    def __init__(self, domain, number_colors, static_colors=[], 
                 max_colors=2048, **kwargs):
        super(Colormap, self).__init__(**kwargs)

        self.cmaps = {}
        for colormap in colormaps:
            self.cmaps[colormap[0]] = colormap[1]

        self.colorbars = {}
        for colorbar, label in colorbars.iteritems():
            self.colorbars[label] = colorbar

        self.colorbars.pop('Blues', None)  #
