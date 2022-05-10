import threading
threading.main_thread()

import base64

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

class Cursor(object):
    _opacity = 1.
    _visible = True

    def __init__(self, fig=None, ax=None, useblit=False, color='k', linewidth=1, linestyle='--', marker='o', markersize=6, text='+', x=0, y=0, active=False, data=None, tolerance=5, vertOn=True, horizOn=True, follow=False):
        """Create a cursor.

        Parameters
        ----------
        fig
        ax
        useblit
        color
        linewidth
        linestyle
        marker
        markersize
        x
        y
        horizOn
        vertOn
        follow

        """
        if fig is None:
            fig = plt.gcf()
            if ax is None:
                ax = plt.gca()
