import weakref

import numpy as np

from ... import format as fmt
from ...tools import (gen_colors, gen_markers, gen_names, get_text_extent,
                      gen_unique_color, find_range)


def backend_show(self):
    if self.fig is None:
        raise RuntimeError('Cannot show the figure, it was closed')
    self.fig.canvas.draw()
    self.fig.canvas.start_event_loop(0.001)


def backend_close(self):
    if self.fig is None:
        raise RuntimeError('Cannot close the figure, it was closed')
    self.fig.canvas.stop_event_loop()
    plt.close(self.fig)


def backend_redraw(self):
    if self.fig is None:
        raise RuntimeError('Cannot redraw the figure, it was closed')
    self.draw()
    self.fig.canvas.draw_idle()


