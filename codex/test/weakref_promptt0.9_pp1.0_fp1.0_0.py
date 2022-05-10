import weakref
# Test weakref.ref(g) == g.weakrepr() == weakrepr(g.__repr__)
weakref.ref(g)
g.weakrepr()
weakrepr(g.__repr__)

import sys
sys.stdout.flush()

# TODO: How to test the following? Maybe by writing out a DATAFILE,
# reading it back in and testing if the __dict__ of the group is the
# same as the one we serialized to the datafile.


#def test_groups_main_dataset_PyTables(self):
#    """Checks main_dataset property of groups"""
#
#    self.assert_(isinstance(self.root.g1.main_dataset, Dataset))
#    self.assert_(self.root.g1._v_children["d1"] is self.root.g1.d1)
#
#    self.assert_(self.root.g1.main_dataset is self.root.g1._v_children["d1"])
#    self.assert_(
