import gc, weakref
from pymol import cmd, CmdException, testing, stored

@testing.requires_version('2.4')
class TestGroups(testing.PyMOLTestCase):

    def _get_group(self, name):
        from pymol import groups
        return groups.get_group(name)

    def _get_group_and_name(self):
        name = 'test'
        group = self._get_group(name)
        return group, name

    def _add_object(self, group, name):
        from pymol import cmd
        cmd.load(self.datafile('1oky-frag.pdb'), name)

    def _remove_object(self, name):
        from pymol import cmd
        cmd.delete(name)

    def _delete_group(self, name):
        from pymol import groups
        groups.delete_group(name)

    def testCreate(self):
        group, name = self._get_group_and_name()
        self.assertIsNone(group)
        self._add_object
