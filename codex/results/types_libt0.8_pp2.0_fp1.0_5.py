import types
types.ClassType = type
types.InstanceType = type

import re

import os
import sys

def merge_dicts(*dicts):
    res = {}
    for d in dicts:
        res.update(d)
    return res

class Dict(dict):
    def __init__(self, **kwargs):
        for k in kwargs:
            self[k] = kwargs[k]

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, val):
        self[name] = val

    def __delattr__(self, name):
        del self[name]

    def __str__(self):
        return str(dict(self))

    def __repr__(self):
        return repr(dict(self))

class Root(object):
    @classmethod
    def _make_global(cls):
        g = Dict(**cls.__dict__)
        del g['__dict__']
        del g['__module__']

