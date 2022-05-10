import gc, weakref
import pdb

from pymol import cmd, CmdException, testing, stored

@testing.requires_version('1.8.3.0')
class TestGarbageCollection(testing.PyMOLTestCase):

    @testing.foreach.product((True, False), (True, False))
    @testing.requires_version('2.0')
    def testModels(self, has_selection, has_refresh):
        cmd.pseudoatom('m1')
        cmd.pseudoatom('m2')
        cmd.pseudoatom('m3')
        cmd.pseudoatom('m4')
        cmd.pseudoatom('m5')
        cmd.pseudoatom('m6')
        cmd.pseudoatom('m7')
        cmd.pseudoatom('m8')
        cmd.pseudoatom('m9')
        cmd.pseudoatom('m10')
        cmd.pseudoatom('m11')
        cmd.pseudoatom('m12')
        cmd.pseudoatom('m13')
        cmd.pseudoatom('m14
