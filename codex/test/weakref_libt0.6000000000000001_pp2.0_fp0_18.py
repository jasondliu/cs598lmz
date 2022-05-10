import weakref

from . import component
from . import entity
from . import system


class World:
    def __init__(self):
        self._components = {}
        self._entities = []
        self._systems = []
        self._events = {}

    def create_entity(self):
        entity_id = len(self._entities)
        self._entities.append(entity.Entity(self, entity_id))
        return self._entities[entity_id]

    def delete_entity(self, entity):
        for system in self._systems:
            system.on_entity_deleted(entity)
        self._entities[entity.id] = None

    def get_component(self, component_type, entity):
        if component_type not in self._components:
            self._components[component_type] = {}
