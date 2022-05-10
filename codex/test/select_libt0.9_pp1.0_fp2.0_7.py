import selective_combinations
import numpy as np


def to_number(string):
    return int(string.split('\n')[0])


def test_combinations():
    assert selective_combinations.generator(to_number('1'), 2, 0) == np.array([
            [],
            []
        ])


def test_combinations_2():
    assert selective_combinations.generator(to_number('1'), 2, 0) == np.array([
        [],
        []
    ])


def test_combinations_3():
    assert selective_combinations.generator(to_number('2'), 2, 0) == np.array([
        [],
        []
    ])

