import mmap
import os
import sys

import numpy as np
import pandas as pd

import openmc


def test_basic():
    batch = openmc.Batch(5)
    assert batch.id == 5
    assert batch.spacing == 'uniform'
    assert batch.distrib_type is None
    assert batch.off_axis == 0.0
    assert batch.filter == []
    assert batch.generations_per_batch == 1
    assert batch.particles == 1
    assert batch.inactive == 0
    assert batch.active == 1

    batch = openmc.Batch(5, spacing='user', distrib_type='point')
    assert batch.id == 5
    assert batch.spacing == 'user'
    assert batch.distrib_type == 'point'
    assert batch.off_axis == 0.0
    assert batch.filter == []
    assert batch.generations_per_batch == 1
    assert batch.particles == 1
    assert batch.inactive == 0
    assert batch.active == 1

    batch = openmc.
