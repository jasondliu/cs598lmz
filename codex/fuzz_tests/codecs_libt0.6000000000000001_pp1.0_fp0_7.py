import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#
# test_get_corpus_statistics_1.py
#
# Copyright © 2016-2017 Monotype Imaging Inc. All Rights Reserved.
#

"""
Support for testing the get_corpus_statistics() function.
"""

# Other imports
from fontio3.fontdata import seqmeta
from fontio3.statistics import get_corpus_statistics

# -----------------------------------------------------------------------------

#
# Test code
#

def _make_f():
    from fontio3.statistics import stats
    return stats.Stats()

def _make_n():
    from fontio3.statistics import stats_naked
    return stats_naked.Stats()

def _make_o():
    from fontio3.statistics import stats_ot
    return stats_ot.Stats()

def _make_c():
    from fontio3.statistics import stats_tt
    return stats_tt.Stats()

def
