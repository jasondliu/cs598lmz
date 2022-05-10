gi = (i for i in ())
# Test gi.gi_code is a function
        self.assertIsInstance(gi.gi_code, types.CodeType)

class TestInstructions(unittest.TestCase):

#  Verify that the instruction opcodes (as attributes of the module) are
#  instructions, and have been given the correct size

    def testOpcodeAttributes(self):
        self.assert_(hasattr(dis, 'opmap'))
        opmap = dis.opmap
        self.assert_(hasattr(opmap, '__getitem__'))
        self.assert_(hasattr(opmap, '__len__'))
        self.assertEqual(len(opmap), dis._count_opcodes())
        self.assert_(hasattr(dis, 'opname'))
        opname = dis.opname
        self.assert_(hasattr(opname, '__getitem__'))
        self.assert_(hasattr(opname, '__len__'))
        self.assertEqual(len(opname), dis._count_opcodes())
        for op in xrange(len(opmap)):

