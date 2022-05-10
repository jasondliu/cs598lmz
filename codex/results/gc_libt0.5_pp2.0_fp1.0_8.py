import gc, weakref

from pymol import cmd, CmdException, testing, stored

class Test1330(testing.PyMOLTestCase):

    @testing.foreach.product((True, False), (True, False), (True, False))
    def test(self, use_mol, use_cmd, use_cmd_str):
        cmd.load(self.datafile("1ehz.pdb"), "m1")

        if use_cmd_str:
            cmd.do("cmd.get_wizard().set_mode('distance')")
            cmd.do("cmd.get_wizard().do_pick(cmd.get_model('m1').atom[1])")

        if use_cmd:
            cmd.get_wizard().set_mode('distance')
            cmd.get_wizard().do_pick(cmd.get_model('m1').atom[1])

        if use_mol:
            m1 = cmd.get_model('m1')
            wizard = cmd.get_wizard()
            wizard.set_mode('distance')
            wizard.do_pick
