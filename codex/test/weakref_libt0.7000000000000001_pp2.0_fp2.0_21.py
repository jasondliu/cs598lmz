import weakref
from uuid import uuid4

from graphql import (
    parse,
    GraphQLError,
    GraphQLID,
    GraphQLNonNull,
    GraphQLSchema,
    GraphQLString,
)
from graphql.type import GraphQLObjectType

from graphene.relay import (
    Connection,
    ConnectionField,
    Edge,
    Node,
    PageInfo,
    Resolver,
    connection_resolver,
)
from graphene.relay.connection import ConnectionType
from graphene.relay.mutation import Mutation as MutationBase
from graphene.relay.node import from_global_id
from graphene.utils.str_converters import to_camel_case
from graphene.utils.is_base_type import is_base_type

from graphene_django.registry import get_global_registry
from graphene_django.converter import convert_django_field
from graphene_django.settings import graphene_settings
from graphene_django.utils import maybe_queryset


