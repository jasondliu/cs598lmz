import gc, weakref
import tinytools.scheduling as sched

import spinmob as sm
_d = sm.data.stored()
_p = sm.plot.get_plotter()
_s = sm.settings.get_saver()
_t = sm.tinytable.get_table()

_p.set_colors(tinyplots=True)
_p.set_markers(tinyplots=True)

def _flush_this():
    _d.flush()
    _t.flush()
    _s.flush()
    _p.flush()
    sched.flush()

############################################################################
class DEPRECATED_PageContainer(object):
    """
    This class is for making and keeping track of pages.
    
    Example:
    
    >>> pages = sm.wizards.PageContainer()
    >>> pages.add_page(ptools.Form([('itm1', 'The Title of this Thing', False)],
                                   title = 'This is a Form',
                                   help  = 'This is some help and it is nice.'))
    

