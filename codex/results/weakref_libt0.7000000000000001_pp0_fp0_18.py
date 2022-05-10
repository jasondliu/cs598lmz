import weakref

# This is a list of weak references to _Entity objects.
weak_entity_list = []


class _Entity(object):
    """Base class for all database-mapped objects."""

    def __init__(self, entity_type, entity_id, attributes,
                 sdk_client=None):
        """Constructor.

        :type entity_type: str
        :param entity_type: The type name of the entity.

        :type entity_id: str
        :param entity_id: The ID of the entity.

        :type attributes: dict
        :param attributes: The attributes of the entity.

        :type sdk_client: :class:`~googlecloudsdk.third_party.apitools.base.py.base_api.BaseApiClient`
        :param sdk_client: The API client used by the entity.
        """
        self._entity_type = entity_type
        self._entity_id = entity_id
        self._attributes = attributes
        self._sdk_client = sdk_client
        self._ref = self
