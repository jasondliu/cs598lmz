import ctypes
ctypes.cast(0, ctypes.py_object)

import sys

sys.path.append('../../')

from pycpptraj.base import *
from pycpptraj import io as mdio
from pycpptraj.utils.check_and_assert import assert_almost_equal

def test_0():
    traj = mdio.load("./data/md1_prod.Tc5b.x", "./data/Tc5b.top")
    frame0 = traj[0]
    frame1 = traj[1]
    frame2 = traj[2]
    print frame0
    print frame1
    print frame2

    assert_almost_equal(frame0.coords[0], frame1.coords[0], decimal=3)
    assert_almost_equal(frame1.coords[0], frame2.coords[0], decimal=3)
    assert_almost_equal(frame0.coords[1], frame1.coords[1], decimal=3)
    assert_almost_equal(frame1.coords[1
