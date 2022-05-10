import weakref

from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator, Panel, PropertyGroup

from .. import utils


class Slides(PropertyGroup):
    def get_slides(self, context):
        try:
            return context.scene.slides.collections
        except AttributeError:
            return []
    name: StringProperty(name="Slide", description="Name of the slide", update=utils.update_slide)
    collection: EnumProperty(name="Collection", description="Collection of objects to show", items=get_slides)
    is_active: BoolProperty(name="Is Active", description="Is this slide currently active", default=False)


class SlidesCollection(PropertyGroup):
    name: StringProperty(name="Collection", description="Name of the collection", update=utils.update_collection)
    is_hidden: BoolProperty(name="Is Hidden", description="Is this collection hidden", default=False)


