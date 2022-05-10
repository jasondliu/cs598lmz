import gc, weakref, sys
import numpy as np
import pytest

import mbuild

def test_compound_creation():
    c = mbuild.Compound(name='test', port_particles=[1, 2, 3])
    assert len(c.children) == 3
    assert c.name == 'test'
    assert c.n_particles == 3
    assert c.n_bonds == 0
    assert c.n_ports == 3
    assert c.n_bond_graph_nodes == 0

def test_creation_with_periodicity():
    c = mbuild.Compound(pos=[0, 0, 0], periodic_box=True)
    assert c.periodic_box
    assert c.children == []
    assert c.n_particles == 1
    assert c.n_bonds == 0

def test_adding_particles():
    c = mbuild.Compound(name='test')
    assert c.n_particles == 0
    c.add('X', 'particle1')
    assert c.n_particles == 1
