import weakref

from synapse.synapse_exceptions import ResourceException

logger = logging.getLogger(__name__)


class ReplicationResource(object):

    def __init__(self, destination, resource_id, resource_name, resources,
                 resource_location, resource_type, version, metadata,
                 content_uri, content, self_link, token_id, token_owner,
                 on_data_ready=None):
        self.destination = destination
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resources = resources

        if resource_location is None:
            resource_location = self.resource_id

        self.resource_location = resource_location
        self.resource_type = resource_type
        self.version = version
        self.metadata = metadata
        self.content_uri = content_uri
        self.content = content
        self.self_link = self_link
        self.token_id = token_id
        self.token_owner = token_owner
        self.on_data_
