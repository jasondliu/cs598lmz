import weakref

from .common import (
    BaseObject,
    BaseObjectList,
    BaseObjectDict,
    BaseObjectSet,
    BaseObjectTuple,
    BaseObjectSetDict,
)


class TestBaseObject:
    def test_base_object(self):
        obj = BaseObject()

    def test_base_object_list(self):
        obj = BaseObjectList()

    def test_base_object_dict(self):
        obj = BaseObjectDict()

    def test_base_object_set(self):
        obj = BaseObjectSet()

    def test_base_object_set_dict(self):
        obj = BaseObjectSetDict()

    def test_base_object_tuple(self):
        obj = BaseObjectTuple()


class TestBaseObjectWeakRef:
    def test_base_object_weakref(self):
        obj = BaseObject()
        obj_ref = weakref.ref(obj)
        assert obj_ref() is obj

    def test_base_object_list_weakref(self):
       
