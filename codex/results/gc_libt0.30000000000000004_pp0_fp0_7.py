import gc, weakref
from pymol import cmd, testing, stored

class Test1577(testing.PyMOLTestCase):

    def test(self):
        cmd.fragment('ala')
        cmd.show_as('sticks')
        cmd.color('red', 'elem C')
        cmd.set('stick_radius', 0.2)
        cmd.set('stick_ball', 0.1)
        cmd.set('stick_ball_ratio', -1)
        cmd.set('stick_quality', 0)
        cmd.set('sphere_scale', 0.1)
        cmd.set('sphere_quality', 0)
        cmd.set('dash_gap', 0)
        cmd.set('dash_width', 0.1)
        cmd.set('dash_radius', 0.1)
        cmd.set('dash_length', 0.5)
        cmd.set('dash_round_ends', 0)
        cmd.set('dash_color', 'red')
        cmd.set('dash_transparency', 0.5)
        cmd.set('dash_as
