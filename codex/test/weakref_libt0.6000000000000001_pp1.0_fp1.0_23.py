import weakref

from ckanext.publicamundi.lib.metadata.base import Object, Metadata
from ckanext.publicamundi.lib.metadata.schemata import MetadataSchema, load_schema, get_schema_from_type, get_schema_from_format
from ckanext.publicamundi.lib.metadata.serializers import (
    MetadataJsonSerializer, MetadataJsonLdSerializer,
    MetadataXmlSerializer,
)
from ckanext.publicamundi.lib.metadata.schemata import get_schemata_names
from ckanext.publicamundi.lib.metadata.schemas.base import Schema
from ckanext.publicamundi.lib.metadata.schemas.simple import SimpleSchema
from ckanext.publicamundi.lib.metadata.schemas.ckan import CkanSchema
from ckanext.publicamundi.lib.metadata.schemas.ckan_metadata import CkanMetadataSchema
