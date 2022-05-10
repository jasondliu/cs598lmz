import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.lines as lines
import matplotlib.collections as collections
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
import matplotlib.transforms as transforms
import matplotlib.text as text
import matplotlib.font_manager as font_manager
import matplotlib.backend_bases as backend_bases
import matplotlib.backends.backend_agg as backend_agg
import matplotlib.backends.backend_pdf as backend_pdf
import matplotlib.backends.backend_svg as backend_svg
import matplotlib.backends.backend_tkagg as backend_tkagg
