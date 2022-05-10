import gc, weakref
from _deque import deque
# Added by Eric.

from sage.rings.all import Integer, QQ, infinity, PolynomialRing, PowerSeriesRing
from sage.groups.all import AbelianGroup
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.element import Element
from sage.modules.all import vector
from sage.graphs.digraph import ImmutableDiGraph
from sage.combinat.words.alphabet import Alphabet
from sage.combinat.free_module import CombinatorialFreeModule

from sage.libs.all import pari

class AlgebraicExtension(Parent):
    """
    This abstract class provides the structure for algebraic
    extensions.
    """

    def __init__(self, base, relation):
        """
        TESTS::

            sage: from sage.rings.polynomial.algebraic_extension import AlgebraicExtension
            sage: k.<a> = AlgebraicExtension(QQ, x^2 + 5, degree=
